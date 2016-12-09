import requests
import bs4

links_list = ['https://www.reddit.com/r/gaming/comments/5e6j8h/some_michael_bay_shit_going_on_right_here/?limit=500', 'https://www.reddit.com/r/gaming/comments/5ckixv/hey_dont_do_that/?limit=500', 'https://www.reddit.com/r/gaming/comments/4ucr3a/making_new_friends_at_a_gaming_convention/?limit=500', 'https://www.reddit.com/r/gaming/comments/5ehto9/2016_in_a_nutshell/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fxu6e/kirby_dev_team_attemps_to_draw_him_by_hand/?limit=500', 'https://www.reddit.com/r/gaming/comments/5gb5au/the_last_of_us_part_ii_announced/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fpxd3/as_long_as_companies_are_taking_adivce_on_nextgen/?limit=500', 'https://www.reddit.com/r/gaming/comments/5akwue/8_months_ago_microsoft_and_sony_both_said_they/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fdu6q/pls_no/?limit=500', 'https://www.reddit.com/r/gaming/comments/5a51e2/ea_games_and_origin_quietly_bans_an_entire/?limit=500', 'https://www.reddit.com/r/gaming/comments/56c8z3/mafia_3s_ingame_statement_on_its_depiction_of/?limit=500', 'https://www.reddit.com/r/gaming/comments/53y133/taking_the_perfect_photograph_in_gta_v/?limit=500', 'https://www.reddit.com/r/gaming/comments/54gyoh/never_forget_good_guy_mario_kart_3ds/?limit=500', 'https://www.reddit.com/r/gaming/comments/5385is/naming_the_new_mobile_game_oc/?limit=500', 'https://www.reddit.com/r/gaming/comments/4wz4rj/i_spent_way_too_much_time_making_this_coloring/', 'https://www.reddit.com/r/gaming/comments/5dm5vl/doom_clay_version/', 'https://www.reddit.com/r/gaming/comments/5gio0t/it_gets_slow_at_work_sometimes_so_i_started/', 'https://www.reddit.com/r/gaming/comments/56xtzr/star_citizen_planet_to_planet_quantum_jumping/', 'https://www.reddit.com/r/gaming/comments/5aqnpd/shadow_warrior_2_understands_why_people_play_on/', 'https://www.reddit.com/r/gaming/comments/5dt3xj/remastered_vs_original/', 'https://www.reddit.com/r/gaming/comments/551wuw/virtual_reality_gaming_booth_at_the_tokyo_game/', 'https://www.reddit.com/r/gaming/comments/5c31na/reddit_today/', 'https://www.reddit.com/r/gaming/comments/5cyqsx/psa_atari_are_releasing_its_incredibly_unfinished/?limit=500', 'https://www.reddit.com/r/gaming/comments/4xtz1q/when_you_realized_you_fucked_up/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fm96m/close_brush_with_death/?limit=500', 'https://www.reddit.com/r/gaming/comments/5c973i/red_alert_2_unreal_engine/?limit=500', 'https://www.reddit.com/r/gaming/comments/51lyfi/my_buddy_and_i_like_to_get_100_on_the_lego_games/?limit=500', 'https://www.reddit.com/r/gaming/comments/53ojtk/you_can_actually_pinpoint_the_year_rockstar/?limit=500', 'https://www.reddit.com/r/gaming/comments/5gn92h/when_you_have_a_long_flight_you_find_a_way/?limit=500', 'https://www.reddit.com/r/gaming/comments/5bfs3h/til_that_the_building_on_the_first_grand_theft/?limit=500', 'https://www.reddit.com/r/gaming/comments/5bsxry/when_the_beat_drops/', 'https://www.reddit.com/r/gaming/comments/5dg511/i_learned_some_sweet_stealth_tactics_from_medal/', 'https://www.reddit.com/r/gaming/comments/5eje7m/let_valve_know/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fu05j/finally_a_ff_character_i_can_cosplay_as/?limit=500', 'https://www.reddit.com/r/gaming/comments/5cqoy7/the_art_critic/?limit=500', 'https://www.reddit.com/r/gaming/comments/5egixc/i_think_its_time_to_retire/?limit=500', 'https://www.reddit.com/r/gaming/comments/5dz0ci/when_you_put_your_vr_headset_on_xpost/?limit=500', 'https://www.reddit.com/r/gaming/comments/5bh8a0/the_most_dedicated_medic_youll_find_xpost/?limit=500', 'https://www.reddit.com/r/gaming/comments/5g2vbq/hideo_kojima_mads_mikkelsen/?limit=500', 'https://www.reddit.com/r/gaming/comments/5gle0r/here_take_it/', 'https://www.reddit.com/r/gaming/comments/5fwcwx/he_fell_for_it/?limit=500', 'https://www.reddit.com/r/gaming/comments/5cdsw2/that_pain/?limit=500', 'https://www.reddit.com/r/gaming/comments/5cpqkx/awesome_frame_rate_truck_mania/?limit=500', 'https://www.reddit.com/r/gaming/comments/4xoxjm/dva_giving_tributing_to_one_of_reddits_most/?limit=500', 'https://www.reddit.com/r/gaming/comments/5ep4p2/perfect_response/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fcwbe/every_fucking_time/?limit=500', 'https://www.reddit.com/r/gaming/comments/5ai7rw/bf1_accident/?limit=500', 'https://www.reddit.com/r/gaming/comments/5cf4ce/you_lost_bro/?limit=500', 'https://www.reddit.com/r/gaming/comments/5bpgv7/the_worlds_most_oblivious_team_ever/?limit=500', 'https://www.reddit.com/r/gaming/comments/54ekbc/took_me_a_minute_to_realize_that_this_was_a/?limit=500', 'https://www.reddit.com/r/gaming/comments/5crzus/pure_evil/?limit=500', 'https://www.reddit.com/r/gaming/comments/52ylrm/this_really_realistic_lemon_and_kitchen_in_the/?limit=500', 'https://www.reddit.com/r/gaming/comments/5fixfq/the_keeper/', 'https://www.reddit.com/r/gaming/comments/5enpy6/ahh_skyrim_guards/?limit=500', 'https://www.reddit.com/r/gaming/comments/54a6md/when_you_play_rocket_league_but_are_only/?limit=500', 'https://www.reddit.com/r/gaming/comments/4qoub9/i_guess_this_kind_of_stuff_does_happen_to_people/?limit=500', 'https://www.reddit.com/r/gaming/comments/5de6hq/drunken_master_style/?limit=500', 'https://www.reddit.com/r/gaming/comments/5gu57y/he_kept_his_promise/?limit=500', 'https://www.reddit.com/r/gaming/comments/59j3lm/back_to_the_future_of_gta/', 'https://www.reddit.com/r/gaming/comments/5dxol4/black_ops_3_logic/?limit=500', 'https://www.reddit.com/r/gaming/comments/5cjlh5/best_part_of_metal_gear_online/?limit=500', 'https://www.reddit.com/r/gaming/comments/5adhf0/trolling_a_dude_whos_just_about_to_drop_in_a/?limit=500']

totalText = ""
for thing in links_list:
    res = requests.get(thing)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    commentTableSet = soup.findAll(True, {'class': ['sitetable', 'nestedlisting']})

    for section in commentTableSet:
        comments = section.select('.md')
        for comment in comments:
            totalText += " "
            totalText += comment.text

    print("Done with: {}").format(thing)

totalText = totalText.replace('\n', ' ')
totalText = ' '.join(totalText.split())

print(totalText)
print("\n\n")
num = len(totalText.split(' '))
print(num)

if num >= 111168:
    myfile = open('gaming.txt', 'w')
    myfile.write(totalText.encode('utf-8'))

# myfile = open('gaming.txt', 'r')
# text = myfile.read()
# print(text)
# print(len(text.split(' ')))