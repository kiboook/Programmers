def solution(skill, skill_trees):
    answer = 0
    data = ""
    i = 0
    # skill과 비교해 있는 스킬만 추출
    for skillTreeCur in skill_trees:
    	for skillTreeIndex in skillTreeCur:
    		if skillTreeIndex in skill:
    				data += skillTreeIndex
    	if data in skill and skill.find(data) == 0:
    		answer += 1
    	data = ""
    return answer