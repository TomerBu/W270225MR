batman_actors = {'Christian Bale', 'Michael Keaton', 'Ben Affleck', 'Robert Pattinson'}

american_actors = {'Christian Bale', 'Ben Affleck', 'Tom Hanks'}

difference = batman_actors.symmetric_difference(american_actors)

print(difference) # {'Robert Pattinson', 'Michael Keaton', 'Tom Hanks'}