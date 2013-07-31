# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table('registration_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('rollno', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('std', self.gf('django.db.models.fields.CharField')(default=1, max_length=50)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('altphone', self.gf('django.db.models.fields.IntegerField')(default=' ', max_length=12, blank=True)),
        ))
        db.send_create_signal('registration', ['Student'])

        # Adding model 'School'
        db.create_table('registration_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone1', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('phone2', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
        ))
        db.send_create_signal('registration', ['School'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table('registration_student')

        # Deleting model 'School'
        db.delete_table('registration_school')


    models = {
        'registration.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone1': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'phone2': ('django.db.models.fields.IntegerField', [], {'max_length': '12'})
        },
        'registration.student': {
            'Meta': {'object_name': 'Student'},
            'altphone': ('django.db.models.fields.IntegerField', [], {'default': "' '", 'max_length': '12', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'std': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '50'})
        }
    }

    complete_apps = ['registration']