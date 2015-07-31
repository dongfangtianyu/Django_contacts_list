#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    SEX_CHOICES = (
        (0, u'未知'),
        (1, u'男'),
        (2, u'女')
    )

    LEVEL_CHOICES = (
        (0, u'实习生'),
        (1, u'普通职员'),
        (2, u'高级职员'),
        (3, u'部门经理'),
        (4, u'总经理')
    )

    STATE_CHOICES = (
        (0, u'离职'),
        (1, u'在职')
    )

    name = models.CharField(max_length=50)
    sex = models.IntegerField(u'性别', default=0, choices=SEX_CHOICES)
    birthday = models.DateTimeField()
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    icq = models.CharField(max_length=20)
    state = models.IntegerField(u'状态', default=1, choices=STATE_CHOICES)
    password = models.CharField(max_length=100)
    level = models.IntegerField(u'职务', default=0, choices=LEVEL_CHOICES)

    def __unicode__(self):
        return self.name

    def get_sex(self):
        if self._sex == 0 :
            return 'man'
        else:
            return 'woman'

    map = {'sex':get_sex}

    def __getattr__(self, item):
        self.map.get(item)()

    # u = User()
    # u.groups
    # u.user_permissions






