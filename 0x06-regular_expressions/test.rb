#!/usr/bin/env ruby
# test
str = "Chez nous, les gens ont généralement deux prénoms, et on les appelle rarement par les deux. On préfère utiliser le premier prénom ou un surnom, mais quand on utilise le nom (par exemple, dans les situations formelles), il faut obligatoirement utiliser les deux prénoms."
regex = /(?<=pré)nom/

str[/surnom/] ? 'Yes' : 'No'
