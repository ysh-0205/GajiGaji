from django.shortcuts import render, redirect
from django.urls import reverse

# 전역 데이터 (임시 저장)
dramas = [
    {"id": 2, "title": "더 글로리", "description": "복수극의 끝판왕.", "image": "01.jpg"},
    {"id": 3, "title": "도깨비", "description": "불멸의 사랑 이야기.", "image": "06.jpg"},
    {"id": 4, "title": "무빙", "description": "초능력 가족 이야기.", "image": "11.jpg"},
    {"id": 5, "title": "악연", "description": "피할 수 없는 운명.", "image": "16.jpg"},
    {"id": 6, "title": "오징어게임1", "description": "생존 서바이벌 게임.", "image": "21.jpg"},
    {"id": 7, "title": "오징어게임2", "description": "서바이벌 게임의 귀환.", "image": "26.jpg"},
    {"id": 8, "title": "오징어게임3", "description": "마지막 서바이벌 게임.", "image": "31.jpg"},
    {"id": 9, "title": "이상한 변호사 우영우", "description": "천재 변호사의 성장기.", "image": "36.jpg"},
    {"id": 10, "title": "중증외상센터", "description": "응급실의 치열한 하루.", "image": "41.jpg"},
    {"id": 11, "title": "파인 촌뜨기들", "description": "시골 생활 적응기.", "image": "46.jpg"},
    {"id": 12, "title": "비밀의 숲", "description": "감정을 잃은 검사와 형사의 추적극.", "image": "51.jpg"},
    {"id": 13, "title": "시그널", "description": "과거와 현재를 연결하는 무전기.", "image": "56.jpg"},

]

# 드라마별 댓글 저장소 (임시)
comments_data = {d["id"]: [] for d in dramas}

def Drama_main(request):
    return render(request, 'Drama/index.html', {"dramas": dramas})

def Drama_detail(request, drama_id):
    # 드라마 찾기
    drama = next((d for d in dramas if d["id"] == drama_id), None)
    if not drama:
        return render(request, 'Drama/detail.html', {
            "drama": {},
            "scenes": [],
            "comments": []
        })

    # 댓글 POST 요청 처리
    if request.method == "POST":
        author = request.POST.get("author")
        content = request.POST.get("content")
        if author and content:
            from datetime import datetime
            comments_data[drama_id].append({
                "author": author,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "content": content
            })
        return redirect(reverse("Drama_detail", args=[drama_id]))

    # 드라마별 scene 번호
    drama_scenes = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10
    }
    scene_num = drama_scenes.get(drama_id, 0)

    scenes = []
    if scene_num:
        scenes = [
            {"image": f"scene{scene_num}_1.jpg"},
            {"image": f"scene{scene_num}_2.jpg"},
            {"image": f"scene{scene_num}_3.jpg"},
            {"image": f"scene{scene_num}_4.jpg"},
        ]

    return render(request, 'Drama/detail.html', {
        "drama": drama,
        "scenes": scenes,
        "comments": comments_data.get(drama_id, [])
    })
