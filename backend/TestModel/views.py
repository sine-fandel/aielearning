from django.shortcuts import render
from django.http import JsonResponse
from xml.etree import cElementTree as ET
import random
import json
from . import models
import hashlib

def hello(request):
  return JsonResponse({'result': 200, 'msg': '连接成功'})

def hash_code(s, salt='ilearning'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())

    return h.hexdigest()

def uploadapi (request) :
  '''
  upload question API
  '''
  if request.method == "POST" :
    req = request.body
    # print (req)
    question = ET.fromstring(req)
    question_info = {}
    question_content = {}
    for question_child in question :
      for child in question_child :
          if question_child.tag == "question_info" :
              question_info[child.tag] = child.text
          else :
              question_content['question_title'] = ET.tostring (question_child)
              break

    print (question_content)
    question_content = models.QuestionContent (question_title=question_content['question_title'])
    question_content.save ()
    question_info = models.QuestionInfo (subject=question_info['subject'], type=question_info['type'], year=question_info['grade'], difficulty=question_info['diffculty'], key_knowledge=question_info['key_knowledge'])
    question_info.save ()

    return JsonResponse({'result': 200, 'msg': 'success'})

def gen_examapi (request) :
  '''
  generate examination API
  '''
  grade = json.loads (request.body.decode()).get ('grade')
  key_knowledge = json.loads (request.body.decode()).get ('key_knowledge')
  difficulty = json.loads (request.body.decode()).get ('difficulty')
  time = json.loads (request.body.decode()).get ('date')
  types = json.loads (request.body.decode()).get ('types')
  types_num = json.loads (request.body.decode()).get ('types_num')
  question_list = []
  answer_list = []
  id_list = []
  questions = ''
  for index in range (0, len (types)) :
    question_info = list (models.QuestionInfo.objects.filter (difficulty=difficulty, type=types[index], key_knowledge=key_knowledge[0]))
    info_list = random.sample (question_info, types_num[index])
    for i in range (0, len (info_list)) :
        id_list.append (info_list[i].question_id)

  for index in range (0, len (id_list)) :
    question_content = list (models.QuestionContent.objects.filter (question_id=id_list[index]))
    question_list.append (question_content[0].question_title)
    answer_list.append (question_content[0].correct_answer)

  for question in question_list :
      questions = questions + question

  exam_xml = '<?xml version="1.0" encoding="utf-8"?>' + '<exam>' + '<start_time>' + time[0] + '</start_time>' + '<end_time>' + time[1] + '</end_time>' + '<exam_questions>' + questions + '</exam_question>' + '</exam>'
  exam_table = models.ExamTable (exam_content=exam_xml, exam_info=grade, exam_answer=answer_list)
  exam_table.save ()

  exam_last = models.ExamTable.objects.all ()
  length = exam_last.count ()
  exam_code = exam_last[length - 1].exam_code

  return JsonResponse ({ 'result': 200, 'msg': 'success', 'code':  exam_code})

def search_examapi (request) :
    '''
    search an exam
    '''
    req = request.body

    exam_content = models.ExamTable.objects.filter (exam_code = req)[0].exam_content
    print (exam_content)

    return JsonResponse ({'result': 200, 'msg': 'success', 'exam_content': exam_content})

def register (request) :
  '''
  register api
  '''
  if request.method == "POST" :
    email = json.loads (request.body.decode()).get ('email')
    password = json.loads (request.body.decode()).get ('password')
    password2 = json.loads (request.body.decode()).get ('password2')
    username = json.loads (request.body.decode()).get ('username')
    birthday = json.loads (request.body.decode()).get ('birthday')
    grade =json.loads (request.body.decode()).get ('grade')
    identity = json.loads (request.body.decode()).get ('identity')

    if password != password2 :
      return JsonResponse ({'result': 200, 'msg': 'The password inputed two times is not the same'})

    else :
      same_username = models.UserTable.objects.filter (username=username)
      if same_username :
        return JsonResponse ({'result': 200, 'msg': 'The username is existed'})

      same_email = models.UserTable.objects.filter (email=email)
      if same_email :
        return JsonResponse ({'result': 200, 'msg': 'The email is existed'})
      
      new_user = models.UserTable.objects.create ()
      new_user.email = email
      new_user.password = hash_code (password)
      new_user.username = username
      new_user.birthday = birthday
      new_user.grade = grade
      new_user.identity = identity
      new_user.save ()

      return JsonResponse ({'result': 200, 'msg': 'success'})
    
def login (request) :
  '''
  login api
  '''
  if request.method == 'POST' :
    email = json.loads (request.body.decode()).get ('email')
    password = json.loads (request.body.decode ()).get ('password')
    user = models.UserTable.objects.filter (email=email)

    if not user :
      return JsonResponse ({'result': 200, 'msg': 'The email address is not registed yet'})
    else :
      if hash_code (password) != user[0].password :
        return JsonResponse ({'result': 200, 'msg': 'wrong password'})
      else :
        username = user[0].username
        return JsonResponse ({'result': 200, 'msg': 'success', 'username': username})


