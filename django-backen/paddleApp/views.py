from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .exception import CustomException
from .tools import handle_upload_file
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
import simplejson
from .models import UserProfile, Ocr_record
from .sentive_filter import filter_sen_txt

@csrf_exempt
@require_http_methods(["POST"])
def paddle_image_upload(request):
  file_info = request.FILES.get('file', None)
  result, detedPath, oriPath, base64_data = handle_upload_file(file_info)
  detect_txt = []

  # 获取检测数据
  for item in result:
    for subItem in item:
      # print(subItem,item)
      detect_txt.append(subItem[1][0])

  after_txt = []
  sen_txt = []

  for text_item in detect_txt:
    item_result, item_sen = filter_sen_txt(text_item)
    if item_sen != "":
      sen_txt.append(item_sen)
      after_txt.append(item_result)

  is_sen = '否'
  if len(sen_txt) > 0:
    is_sen = "是"

  after_txt_result = ";".join(after_txt)
  sen_txt_result = ";".join(sen_txt)

  # print("识别字符", detect_txt)
  # print("是否敏感字符", is_sen)
  # print("敏感字符", sen_txt)
  # print("敏感字符结果", sen_txt_result)

  ocr_record = Ocr_record(
    image=base64_data,
    is_sen=is_sen,
    sen_txt=sen_txt_result,
    after_txt=after_txt_result,
    text=';'.join(detect_txt))
  ocr_record.save()

  return JsonResponse({
    'code': 0,
    'message': 'SUCCESS',
    'data': {
      'result': result,
      'sen_txt': sen_txt,
      'after_txt': after_txt,
      'is_sen': is_sen,
      'txt': ocr_record.text
    }
  })


# 登录接口
@csrf_exempt
@require_http_methods(["POST"])
def logins(request):
  receive_data = simplejson.loads(request.body)

  if not receive_data:
    return CustomException(msg="请求数据为空").get()

  user_name = receive_data['username']
  pass_word = receive_data['password']
  user_file = UserProfile.objects.filter(user_name=user_name).exists()

  if not user_file:
    return JsonResponse({'code': 401, 'message': '账号或密码错误', "data": None}, status=401)
  else:
    user_file = UserProfile.objects.get(user_name=user_name)
    if (user_file.pass_word != pass_word):
      return JsonResponse({'code': 401, 'message': '账号或密码错误', "data": None}, status=401)

  token = "awercdsr" + user_name + "123"

  return JsonResponse(
    {
      'code': 0,
      'message': '登录成功',
      'token': token,
      'userProfile': ''
    })


# 注册接口
@csrf_exempt
@require_http_methods(["POST"])
def register(request):
  receive_data = simplejson.loads(request.body)

  if not receive_data:
    return CustomException(msg="请求数据为空").get()

  user_name = receive_data['username']
  confrim_pass_word = receive_data['confirm_password']
  print("user name 为", user_name, "confirm_pass_word is ", confrim_pass_word)

  user_file = UserProfile.objects.filter(user_name=user_name).exists()
  if user_file:
    return JsonResponse({'code': 401, 'message': '账号已存在，注册失败', "data": None}, status=401)
  else:
    user_file = UserProfile(user_name=user_name, pass_word=confrim_pass_word)
    user_file.save()

  return JsonResponse(
    {
      'code': 0,
      'message': '注册成功',
      'userProfile': ''
    })


# 注册接口
@csrf_exempt
@require_http_methods(["POST"])
def delete_record(request):
  receive_data = simplejson.loads(request.body)

  if not receive_data:
    return CustomException(msg="请求数据为空").get()
  id = receive_data['id']

  result = Ocr_record.objects.filter(id=id).delete()
  print("result is", result)

  return JsonResponse(
    {
      'code': 0,
      'message': '删除成功',
    })


# 获取列表
@csrf_exempt
@require_http_methods(["GET"])
def one_ocr_record(request):
  page = request.GET.get("page")
  limit = request.GET.get("limit")

  sys_user_list = Ocr_record.objects.order_by("-create_at").all().values()
  pageinator = Paginator(sys_user_list, per_page=limit)

  page_list = pageinator.page(page)
  return JsonResponse(
    {
      'code': 0,
      'message': '登录成功',
      'data': list(page_list.object_list.all().values()),
      "totalPage": pageinator.count,
    })
