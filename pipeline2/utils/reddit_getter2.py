import requests
import pyperclip
import praw

#https://www.reddit.com/r/gaming/comments/5e6j8h/some_michael_bay_shit_going_on_right_here/
#https://www.reddit.com/r/gaming/comments/5ckixv/hey_dont_do_that/
#https://www.reddit.com/r/gaming/comments/4ucr3a/making_new_friends_at_a_gaming_convention/
#https://www.reddit.com/r/gaming/comments/5ehto9/2016_in_a_nutshell/
#https://www.reddit.com/r/gaming/comments/5fxu6e/kirby_dev_team_attemps_to_draw_him_by_hand/
#https://www.reddit.com/r/gaming/comments/5gb5au/the_last_of_us_part_ii_announced/
#https://www.reddit.com/r/gaming/comments/5fpxd3/as_long_as_companies_are_taking_adivce_on_nextgen/
#https://www.reddit.com/r/gaming/comments/5akwue/8_months_ago_microsoft_and_sony_both_said_they/
#https://www.reddit.com/r/gaming/comments/5fdu6q/pls_no/
#https://www.reddit.com/r/gaming/comments/5a51e2/ea_games_and_origin_quietly_bans_an_entire/
#https://www.reddit.com/r/gaming/comments/56c8z3/mafia_3s_ingame_statement_on_its_depiction_of/
#https://www.reddit.com/r/gaming/comments/53y133/taking_the_perfect_photograph_in_gta_v/
#https://www.reddit.com/r/gaming/comments/54gyoh/never_forget_good_guy_mario_kart_3ds/
#https://www.reddit.com/r/gaming/comments/5385is/naming_the_new_mobile_game_oc/
#https://www.reddit.com/r/gaming/comments/4wz4rj/i_spent_way_too_much_time_making_this_coloring/
#https://www.reddit.com/r/gaming/comments/5dm5vl/doom_clay_version/
#https://www.reddit.com/r/gaming/comments/5gio0t/it_gets_slow_at_work_sometimes_so_i_started/
#https://www.reddit.com/r/gaming/comments/56xtzr/star_citizen_planet_to_planet_quantum_jumping/
#https://www.reddit.com/r/gaming/comments/5aqnpd/shadow_warrior_2_understands_why_people_play_on/
#https://www.reddit.com/r/gaming/comments/5dt3xj/remastered_vs_original/
#https://www.reddit.com/r/gaming/comments/551wuw/virtual_reality_gaming_booth_at_the_tokyo_game/
#https://www.reddit.com/r/gaming/comments/5c31na/reddit_today/
#https://www.reddit.com/r/gaming/comments/5cyqsx/psa_atari_are_releasing_its_incredibly_unfinished/
#https://www.reddit.com/r/gaming/comments/4xtz1q/when_you_realized_you_fucked_up/
#https://www.reddit.com/r/gaming/comments/5fm96m/close_brush_with_death/
#https://www.reddit.com/r/gaming/comments/5c973i/red_alert_2_unreal_engine/
#https://www.reddit.com/r/gaming/comments/51lyfi/my_buddy_and_i_like_to_get_100_on_the_lego_games/
#https://www.reddit.com/r/gaming/comments/53ojtk/you_can_actually_pinpoint_the_year_rockstar/
#https://www.reddit.com/r/gaming/comments/5gn92h/when_you_have_a_long_flight_you_find_a_way/
#https://www.reddit.com/r/gaming/comments/5bfs3h/til_that_the_building_on_the_first_grand_theft/
#https://www.reddit.com/r/gaming/comments/5bsxry/when_the_beat_drops/
#https://www.reddit.com/r/gaming/comments/5dg511/i_learned_some_sweet_stealth_tactics_from_medal/
#https://www.reddit.com/r/gaming/comments/5eje7m/let_valve_know/
#https://www.reddit.com/r/gaming/comments/5fu05j/finally_a_ff_character_i_can_cosplay_as/
#https://www.reddit.com/r/gaming/comments/5cqoy7/the_art_critic/
#https://www.reddit.com/r/gaming/comments/5egixc/i_think_its_time_to_retire/
#https://www.reddit.com/r/gaming/comments/5dz0ci/when_you_put_your_vr_headset_on_xpost/
#https://www.reddit.com/r/gaming/comments/5bh8a0/the_most_dedicated_medic_youll_find_xpost/
#https://www.reddit.com/r/gaming/comments/5g2vbq/hideo_kojima_mads_mikkelsen/
#https://www.reddit.com/r/gaming/comments/5gle0r/here_take_it/
#https://www.reddit.com/r/gaming/comments/5fwcwx/he_fell_for_it/
#https://www.reddit.com/r/gaming/comments/5cdsw2/that_pain/
#https://www.reddit.com/r/gaming/comments/5cpqkx/awesome_frame_rate_truck_mania/
#https://www.reddit.com/r/gaming/comments/4xoxjm/dva_giving_tributing_to_one_of_reddits_most/
#https://www.reddit.com/r/gaming/comments/5ep4p2/perfect_response/
#https://www.reddit.com/r/gaming/comments/5fcwbe/every_fucking_time/
#https://www.reddit.com/r/gaming/comments/5ai7rw/bf1_accident/
#https://www.reddit.com/r/gaming/comments/5cf4ce/you_lost_bro/
#https://www.reddit.com/r/gaming/comments/5bpgv7/the_worlds_most_oblivious_team_ever/
#https://www.reddit.com/r/gaming/comments/54ekbc/took_me_a_minute_to_realize_that_this_was_a/
#https://www.reddit.com/r/gaming/comments/5crzus/pure_evil/
#https://www.reddit.com/r/gaming/comments/52ylrm/this_really_realistic_lemon_and_kitchen_in_the/
#https://www.reddit.com/r/gaming/comments/5fixfq/the_keeper/
#https://www.reddit.com/r/gaming/comments/5enpy6/ahh_skyrim_guards/
#https://www.reddit.com/r/gaming/comments/54a6md/when_you_play_rocket_league_but_are_only/
#https://www.reddit.com/r/gaming/comments/4qoub9/i_guess_this_kind_of_stuff_does_happen_to_people/
#https://www.reddit.com/r/gaming/comments/5de6hq/drunken_master_style/
#https://www.reddit.com/r/gaming/comments/5gu57y/he_kept_his_promise/
#https://www.reddit.com/r/gaming/comments/59j3lm/back_to_the_future_of_gta/
#https://www.reddit.com/r/gaming/comments/5dxol4/black_ops_3_logic/
#https://www.reddit.com/r/gaming/comments/5cjlh5/best_part_of_metal_gear_online/
#https://www.reddit.com/r/gaming/comments/5adhf0/trolling_a_dude_whos_just_about_to_drop_in_a/

def get_comments(reddit, link_id):
    """Returns a list of comments from a thread with the given link id"""
    comments = []

    submission = reddit.submission(id=link_id)
    submission.comments.replace_more(limit=0)
    comment_queue = submission.comments[:] # Seed with top-level
    while comment_queue:
        comment = comment_queue.pop(0)
        comments.append(comment.body)
        comment_queue.extend(comment.replies)

    print("Link done: ", link_id)
    return comments

def get_comments_from_list(reddit, links_list):
    """Returns a list of comments from the given list of links to threads"""
    comments = []
    for link in links_list:
        link_comments = get_comments(reddit, link)
        if link_comments is not None:
            comments.extend(link_comments)

    return comments

def main():
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/argh_k)',
                         client_id='Jp3J50sb3ucOqQ', client_secret="lSye-_q7JiF6dEQMHp2cl6RJ_UY",
                         username='wowthisisabotman')

    links_list = ['5adhf0', '5cjlh5', '5dxol4', '59j3lm', '5gu57y', '5de6hq', '4qoub9', '54a6md', '5enpy6', '5fixfq', '5fixfq', '52ylrm', '5crzus', '5e6j8h', '5ckixv', '4ucr3a','5ehto9','fxu6e','5gb5au','5fpxd3','5akwue','5fdu6q','5a51e2','56c8z3','53y133','54gyoh','5385is','4wz4rj','5dm5vl','5gio0t','56xtzr','5aqnpd','5dt3xj','551wuw','5c31na','5cyqsx','4xtz1q','5fm96m','5c973i','51lyfi','53ojtk','5gn92h','5bfs3h','5bsxry','5dg511','5eje7m','5fu05j','5cqoy7','5egixc','5dz0ci','5bh8a0','5g2vbq','5gle0r','5fwcwx','5cdsw2','5cpqkx','4xoxjm','5ep4p2','fcwbe','5ai7rw','5cf4ce','5bpgv7','54ekbc']
    
    comments = get_comments_from_list(reddit, links_list)
    return comments

if __name__ == '__main__':
    comments = ' '.join(main())
    pyperclip.copy(comments)

    comments = comments.encode('utf-8').strip()
    textfile = open('temptemp.txt', 'w')
    textfile.write(comments)

    print(len(comments))
    num = 0
    for comment in comments:
        num += len(comment.split(' '))
    print(num)
