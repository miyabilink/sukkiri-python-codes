member_hobbies = {
    '松田': {'SNS', '麻雀', '自転車'},
    '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies) # 2人に共通する趣味一覧を表示する