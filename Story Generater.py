import random
when = ["Yesterday", "Today", "Tommorrow", "Last week", "Next week", "This week", "Last month", "This month", "Next month", "Last year", "This year", "Next year"]
who = ["the Tarbosaurus ", "the Brachiosaurus ", "the Tyrannosaurus Rex ", "the Carnotaurus ", "the Sinoceratops ", "the Baryonyx ", "the Ankylosaurus "]
name = ["Krithik","Kamu","Joe", "Abdullah", "Rakan", "Jonathan", "Moez", "Yadav"]
residence = ["India","UAE", "England", "Kuwait", "Morroco", "Spain", "Switzerland", "France", "Germany", "Scotland"]
went = ["cinema", "city", "pangea", "restaurant", "Museum of Natural History", "Expo 2020", "school", "the beach", "a fossil dig site"]
happened = ["watched a movie", "saw famous tourist attractions", "discovered a dinosaur fossil", "ate some McDonalds food", "learnt about the Mesozoic era", "learnt about different countries", "played laser tag", "built a sand castle"]
print(random.choice(when) +', '+ random.choice(who) + ', ' + 'whose name was '+ random.choice(name) + ' and' +' who lived in ' + random.choice(residence) + ',' + ' went to ' + random.choice(went) + ' and ' + random.choice(happened))