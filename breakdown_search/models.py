from __future__ import unicode_literals

from django.db import models


class Node(models.Model):
    car_model = models.ForeignKey("cars.CarModel", null=True, blank=True)
    answer_text = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=200, blank=True)
    node_text = models.TextField(max_length=1000, blank=True)
    root_node = models.ForeignKey("self", null=True, blank=True)
    instruction = models.ForeignKey("InstructionStep", null=True, blank=True)
    root = models.BooleanField(default=False)

    def __unicode__(self):
        return self.node_text

    def as_dict(self):
        return {
            'id': self.id,
            'answer_text': self.answer_text,
            'name': self.name,
            'node_text': self.node_text,
            'root': self.root,
            'instruction': self.instruction
        }


class InstructionStep(models.Model):
    text = models.TextField(max_length=1000, blank=True)
    next_step = models.ForeignKey("self", null=True, blank=True)