#genres = ["classic", "pop", "classic", "classic", "pop"]
#plays = [500, 600, 150, 800, 2500]
genres = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays = [2000, 500, 600, 150, 800, 2500, 2000]
# 정답 = [0, 6, 5, 2, 4, 1]
def get_melon_best_album(genre_array, play_array):
    length=len(genre_array)
    genre_list=set(genre_array)
    answer_list=[]
    dict_genre_plays_sums={}
    dict_genre_index_plays={}
    for i in range(len(genre_list)):
        dict_genre_plays_sums.update({genre_array[i]:0})
        dict_genre_index_plays[genre_array[i]] = []
    for i in range(length):
        dict_genre_plays_sums[genre_array[i]]+=play_array[i]
        dict_genre_index_plays[genre_array[i]].append((i, play_array[i]))

    genre_sorted_by_plays_sum = sorted(dict_genre_plays_sums.items(), key=lambda item: item[1], reverse=True)

    for items,v in genre_sorted_by_plays_sum:
        dict_genre_index_plays[items].sort(key=lambda item:(-item[1], item[0]))
    for items,v in genre_sorted_by_plays_sum:
        answer_list.append(dict_genre_index_plays[items][0][0])
        answer_list.append(dict_genre_index_plays[items][1][0])
    return answer_list


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!