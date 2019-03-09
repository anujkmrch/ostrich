# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse

def getLightStatus():
	return JsonResponse({'foo':'bar'})

def getCameraDensity():
	return JsonResponse({'foo':'bar'})
