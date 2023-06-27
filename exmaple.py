@app.route('/log_play/<game_id>/save/<names_list_json>/<scores>', methods=['GET', 'POST'])
def save_results_in_table(game_id, names_list_json, scores): 
    """Saves Results to match_player Table"""
   
    match_id = 40
    list_scores = [3, 12, 15]
    false_if_not_greater_than_all(list_scores)
    #  THIS IS WHERE I AM GETTING THE ERROR ABOUT THE RETURN STATEMENT IT NEEDS A RETURN STATEMENT AND I THOUGHT I COULD NEST THE FUNCTION
    # AND THEN PLACE THE RETURN STATEMENT AT THE VERY BOTTOM. BUT IF I DO THAT I HAVE TO INDENT MY FUNCTIONS AND THEN I RETURN A 
    # UnboundLocalError: local variable 'false_if_not_greater_than_all' referenced before assignment
    #IF I ADD A RETURN STATEMENT MY FUNCTIONS ARE ONLY CALLED ONCE AND THEREFORE I AM ONLY GETTING ONE OF THE MATCH_PLAYER IN MY DATABASE BECAUSE 
    # IT IS IMMEDIATELY REDIRECTING TO THE NEXT ROUTE AND NOT ENTERING ALL THE DATA
    

def false_if_not_greater_than_all(list_scores):
    _list_scores = list_scores.copy()
    greatest, is_greater_than_all = check_if_greater_than_all(_list_scores)
    print(map_greatest(list_scores, greatest, is_greater_than_all))
    return map_greatest(list_scores, greatest, is_greater_than_all)

def map_greatest(list_scores, greatest: int, is_greater_than_all):
   
    list_wins = [is_greater_than_all if score == greatest else False for score in list_scores]
    finish_route(list_wins, list_scores)
    
def finish_route(list_wins, list_scores):
    players_ids = session['players_ids_list']
    match_id = session['match_id']
    
    max_length = (max(len(players_ids), len(list_wins), len(list_scores)))
    
    for i in range(max_length):
        new_match_player = match_player.insert().values(match_id=match_id, player_id=players_ids[i], win=list_wins[i], score=list_scores[i])

        try:
            db.session.execute(new_match_player)
            db.session.commit()
            return redirect('/match/results')
            
        except IntegrityError:
            pass
            return redirect('/match/results')
    return redirect('/match/results')
