#ID Number: 205833
#Surname: Co
#Year and Course: 2 BS ITE

#Problem 1
def problem_1(message, shift):
    l = []

    for i in message:
        if i == " ":
            l.append(" ")
        else:
            x = ord(i) + shift
            while x > 90:
                x -= 26
            else:
                l.append(chr(x))

    a = "".join(l)
    return a

print(problem_1("ATTACK AT DAWN", 3))

#Problem 2
def relationship_status(from_member, to_member, social_graph):
    if (from_member in social_graph[to_member]["following"]) and (
        to_member in social_graph[from_member]["following"]
    ):
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    else:
        return None
    
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

print(relationship_status("@joeilagan","@jobenilagan",social_graph))

#Problem 3
def tic_tac_toe(board):
    dimensions = len(board)

    for i in range(0, dimensions):
        if len(set(board[i])) == 1:
            if board[i][0] == "X":
                return "X"
            if board[i][0] == "O":
                return "O"

        l = []
        for j in range(0, dimensions):
            l.append(board[j][i])
        if len(set(l)) == 1:
            if board[0][i] == "X":
                return "X"
            if board[0][i] == "O":
                return "O"

    diag1 = []
    diag2 = []
    for k in range(0, dimensions):
        diag1.append(board[k][k])
        diag2.append(board[k][dimensions - k - 1])
    if len(set(diag1)) == 1:
        if board[0][0] == "X":
            return "X"
        if board[0][0] == "O":
            return "O"
    elif len(set(diag2)) == 1:
        if board[0][dimensions - 1] == "X":
            return "X"
        if board[0][dimensions - 1] == "O":
            return "O"
    else:
        return None
    
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

print(tic_tac_toe(board1))

#Problem 4
def eta(legs, source, destination):
    time = 0
    dimensions = len(legs)
    keys = list(legs.keys())
    values = list(legs.values())

    for i in range(0, dimensions):
        if keys[i][0] == source and keys[i][1] == destination:
            time = values[i]["travel_time_mins"]
            return time
        elif keys[i][0] == source:
            x = i
            while keys[x][1] != destination:
                time += values[x]["travel_time_mins"]
                if x < dimensions - 1:
                    x += 1
                else:
                    x = 0
            time += values[x]["travel_time_mins"]

    return time

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

print(eta(legs,"upd","dlsu"))

