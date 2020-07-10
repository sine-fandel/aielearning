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
        if question_child.tag == "correct_answer" or question_child.tag == "explanation" :
            question_content[question_child.tag] = question_child.text
        else :
            for child in question_child :
                if question_child.tag == "question_info" :
                    question_info[child.tag] = child.text
                else :
                    question_content['question_title'] = ET.tostring (question_child)
                    break

    print (question_content)
    question_content = models.QuestionContent (question_title=question_content['question_title'], correct_answer=question_content['correct_answer'], explanation=question_content['explanation'])
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

    return JsonResponse({'result': 200, 'msg': 'success', 'exam_content': exam_content})





