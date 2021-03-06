# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View
from .models import CourseOrganization, City
from django.shortcuts import render
from courses.models import Course
from pure_pagination import Paginator, PageNotAnInteger


class OrganizationDetailHomepageView(View):
    def get(self, request, org_id):
        organization = CourseOrganization.objects.get(id=org_id)
        show_courses = organization.course_set.all()[:3]
        show_introduce = organization.describe
        show_teachers = organization.teacher_set.all()[:3]
        page_type = request.GET.get('page_type', '')
        return render(request, template_name='org-detail-homepage.html', context={
            'org_id': org_id,
            'organization': organization,
            'show_courses': show_courses,
            'show_introduce': show_introduce,
            'show_teachers': show_teachers,
            'page_type': page_type
        })


class OrganizationDetailIntroduceView(View):
    def get(self, request, org_id):
        organization = CourseOrganization.objects.get(id=org_id)
        introduce = organization.describe
        page_type = request.GET.get('page_type', '')
        return render(request, template_name='org-detail-desc.html', context={
            'introduce': introduce,
            'org_id': org_id,
            'page_type': page_type
        })


class OrganizationDetailCourseView(View):
    def get(self, request, org_id):
        organization = CourseOrganization.objects.get(id=org_id)
        all_courses = organization.course_set.all()
        page = request.GET.get('page', 1)
        p = Paginator(all_courses, 1, request=request)
        page_objs = p.page(page)
        page_type = request.GET.get('page_type', '')
        return render(request, template_name='org-detail-course.html', context={
            'page_objs': page_objs,
            'org_id': org_id,
            'page_type': page_type
        })


class OrganizationDetailTeacherView(View):
    def get(self, request, org_id):
        page_type = request.GET.get('page_type', '')
        organization = CourseOrganization.objects.get(id=org_id)
        all_teachers = organization.teacher_set.all()
        return render(request, template_name='org-detail-teachers.html', context={
            'all_teachers': all_teachers,
            'org_id': org_id,       # NoReverseMatch: Reverse for 'organization_detail_homepage' with arguments '('',)'
                                    # and keyword
            'page_type': page_type, # arguments '{}' not found. 1 pattern(s) tried: ['organization_detail_homepage/(
                                    # ?P<org_id>\\d+)/$'] 如果没有org_id会报错
        })


class OrganizationListView(View):
    def get(self, request):
        all_organization = CourseOrganization.objects.all()
        org_count = all_organization.count()
        all_city = City.objects.all()

        # 筛选出所选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_organization = all_organization.filter(city_id=int(city_id))
        # 筛选课程机构类型
        org_type = request.GET.get('org_type', '')
        if org_type:
            all_organization = all_organization.filter(organization_type=org_type)
        # 按学生人数排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_organization = all_organization.order_by('-study_number')
        # 按课程数排序
        sort = request.GET.get('sort', '')
        if sort == 'courses':
            all_organization = all_organization.order_by('-course_number')
        page_obj = _page_object(request, model_object=all_organization)
        # 按点击量对课程机构进行排序
        hot_orgs = CourseOrganization.objects.order_by('-click_nums')[:3]
        return render(request, template_name='org-list.html', context={
            'page_obj': page_obj,
            'all_city': all_city,
            'org_count': org_count,
            'city_id': city_id,
            'org_type': org_type,
            'sort': sort,
            'hot_orgs': hot_orgs
        })


def _page_object(request, model_object):
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(model_object, 2, request=request)
    page_obj = p.page(page)
    return page_obj