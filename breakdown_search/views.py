from django.http import HttpResponseBadRequest, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from breakdown_search.models import Node, InstructionStep
from cars.models import CarBrand


class BreakdownSearch(TemplateView):
    template_name = 'breakdown_search_alg.html'

    def get_context_data(self, **kwargs):
        context = {
            'cars_brands': CarBrand.objects.all()
        }
        return context


class GetRootNode(View):
    def get(self, request):
        try:
            model_id = int(request.GET.get('model'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        # node = Node.objects.filter(root=True, car_model=model_id).first()
        node = get_object_or_404(Node, root=True, car_model=model_id)
        return JsonResponse({
            'node': node.as_dict(),
            'answers': [{'id': answer.id, 'text': answer.answer_text} for answer in node.node_set.all()]
        })

class TreeSearch(View):
    def get(self, request):
        try:
            node_id = int(request.GET.get('node_id'))
            node = get_object_or_404(Node, id=node_id)
        except (ValueError, TypeError):
            node = Node.objects.filter(root=True).first()
        context = {'node': node.as_dict(),
                   'answers': [{'id': answer.id, 'text': answer.answer_text} for answer in node.node_set.all()]}
        return JsonResponse(context)

class GetPrevNode(View):
    def get(self, request):
        try:
            node_id = int(request.GET.get('node_id'))
            node = get_object_or_404(Node, id=node_id)
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        node = node.root_node
        if not node:
            return Http404()
        context = {'node': node.as_dict(),
                   'answers': [{'id': answer.id, 'text': answer.answer_text} for answer in node.node_set.all()]}
        return JsonResponse(context)


class GetInstruction(View):
    def get(self, request):
        try:
            step_id = int(request.GET.get('step_id'))
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        step = get_object_or_404(InstructionStep, id=step_id)
        steps = [step.as_dict()]
        while step.next_step:
            step = step.next_step
            steps.append(step.as_dict())
        return JsonResponse({'steps': steps})
