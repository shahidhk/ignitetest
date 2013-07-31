# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'School.phone2'
        db.alter_column('registration_school', 'phone2', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'School.phone1'
        db.alter_column('registration_school', 'phone1', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'School.mobile'
        db.alter_column('registration_school', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Student.altphone'
        db.alter_column('registration_student', 'altphone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'Student.phone'
        db.alter_column('registration_student', 'phone', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Student.email'
        db.alter_column('registration_student', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

    def backwards(self, orm):

        # Changing field 'School.phone2'
        db.alter_column('registration_school', 'phone2', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'School.phone1'
        db.alter_column('registration_school', 'phone1', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'School.mobile'
        db.alter_column('registration_school', 'mobile', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'Student.altphone'
        db.alter_column('registration_student', 'altphone', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'Student.phone'
        db.alter_column('registration_student', 'phone', self.gf('django.db.models.fields.IntegerField')(max_length=12))

        # Changing field 'Student.email'
        db.alter_column('registration_student', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))

    models = {
        'registration.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'registration.student': {
            'Meta': {'object_name': 'Student'},
            'altphone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'std': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'})
        }
    }

    complete_apps = ['registration']