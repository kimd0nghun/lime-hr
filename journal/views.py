import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from mdm.models import EvalPlan, AbltEvalRslt, EvalRel
from evaluation.serializers import EvalPlanSerializer, AbltEvalRsltSerializer
from django.utils.http import urlencode
from django.template.loader import render_to_string
from config.utils import dict_fetchall, count_fetchall
from management.models import CommCd
from accounts.models import EusoMem
from django.db import transaction


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_journal(request, *args, **kwargs):
    result = dict(**kwargs)

    return render(request, 'journal/journal_main.html', result)
