from django.http import HttpResponseBadRequest, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
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
        node = get_object_or_404(Node, root=True, car_model=model_id)
        request.session['history'] = [node.id]
        return JsonResponse({
            'node': node.as_dict(),
            'answers': [{'id': answer.id, 'text': answer.answer_text} for answer in node.node_set.all()]
        })


class TreeSearch(View):
    def get(self, request):
        try:
            node_id = int(request.GET.get('node_id'))
            node = get_object_or_404(Node, id=node_id)
            root_node = int(request.GET.get('root_node', 0))
            mileage = int(request.GET.get('mileage', 9999999))
            if mileage == 0:
                mileage = 9999999
        except (ValueError, TypeError):
            return HttpResponseBadRequest()
        l = request.session['history']
        l.append(node.id)
        request.session['history'] = l
        context = {'node': node.as_dict(mileage=mileage),
                   'answers': [{'id': answer.id, 'text': answer.answer_text} for answer in node.node_set.all() if answer.mileage <= mileage and answer.low_mileage >= mileage],
                   'root_node': root_node}
        return JsonResponse(context)


class GetPrevNode(View):
    def get(self, request):
        l = request.session['history']
        l.pop()
        node = get_object_or_404(Node, id=l[-1])
        request.session['history'] = l
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
