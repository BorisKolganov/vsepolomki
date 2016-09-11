from django.http import HttpResponseBadRequest, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from breakdown_search.models import Node


class BreakdownSearch(TemplateView):
    template_name = 'breakdown_search_alg.html'

    def dispatch(self, request, *args, **kwargs):
        print 'lol'
        return super(BreakdownSearch, self).dispatch(request, *args, **kwargs)


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