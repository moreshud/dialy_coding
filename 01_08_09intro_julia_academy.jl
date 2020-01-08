#cell running
1 + 1
2 + 2

1 + 1
2 + 2; #no output display

?println #help function
;ls #shell commands
;pwd #shell commands

#strings
s1 = "I am a string."
s2 = """I am also a string. """
s3 = 'I am not a string so expect Error'

"""Look, Mom, no "errors"!!! """
typeof('a') #var type

#string interpolation
name = "Jane"
num_fingers = 10
num_toes = 10
println("Hello, my name is $name.")
println("I have $num_fingers fingers and $num_toes toes.")
println("That is $(num_fingers + num_toes) digits in all!!")

s3 = "How many cats ";
s4 = "is too many cats?";
😺 = 10

#string concatenation
string(s3, s4)
string("I don't know, but ", 😺, " is too few.")
s3*s4


#data structures
#-tuples and Namedtuples
myfavoriteanimals = ("penguins", "cats", "sugargliders")
myfavoriteanimals[1]
myfavoriteanimals[1] = "otters" #immutate so Error

myfavoriteanimals = (bird = "penguins", mammal = "cats", marsupial = "sugargliders")
typeof(myfavoriteanimals)
myfavoriteanimals[1]
myfavoriteanimals.bird
myfavoriteanimals.bird == myfavoriteanimals.mammal

#-dictionary
myphonebook = Dict("Jenny" => "867-5309", "Ghostbusters" => "555-2368")
myphonebook["Jenny"] #index only by name
myphonebook["Kramer"] = "555-FILK" #mutable
myphonebook
pop!(myphonebook, "Kramer")

#-arrays
myfriends = ["Ted", "Robyn", "Barney", "Lily", "Marshall"]
fibonacci = [1, 1, 2, 3, 5, 8, 13]
mixture = [1, 1, 2, 3, "Ted", "Robyn"]
myfriends[3] = "Baby Bop" #mutable
push!(fibonacci, 21)
favorites = [["koobideh", "chocolate", "eggs"],["penguins", "cats", "sugargliders"]]
numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

rand(4, 3)
rand(4, 3, 2)

#becareful when you copy array because of its modification
somenumbers = fibonacci
somenumbers[1] = 404
fibonacci, somenumbers #both somenumbers and fibonacci are updated together
fibonacci[1] = 1 #resore the number to 1
somemorenumbers = copy(fibonacci)
somemorenumbers[1] = 404
fibonacci, somemorenumbers

#Exercises
a_ray = [1, 2, 3]
push!(a_ray, 4); pop!(a_ray)
@assert a_ray == [1, 2, 3]

myphonebook
myphonebook["Emergency"] = "911" 
myphonebook["Emergency"] = 911 #Error because the parent dict_value homogeneous

flexible_phonebook = Dict("Jenny" => 8675309, "Ghostbusters" => "555-2368")
@assert flexible_phonebook == Dict("Jenny" => 8675309, "Ghostbusters" => "555-2368")
flexible_phonebook["Emergency"] = 911 #Works! since its parent dic_value is heterogeneous

@assert haskey(flexible_phonebook, "Emergency")
@assert flexible_phonebook["Emergency"] == 911


#Loops
n = 0
while n < 10
    n += 1
    println(n)
end
n

myfriends = ["Ted", "Robyn", "Barney", "Lily", "Marshall"]

i = 1
while i <= length(myfriends)
    friend = myfriends[i]
    println("Hi $friend, it's great to see you!")
    i += 1
end

for n in 1:10
    println(n)
end

for friend in myfriends
    println("Hi $friend, it's great to see you!")
end

m, n = 5, 5
A = fill(0, (m, n))

for i in 1:m
    for j in 1:n
        A[i, j] = i + j
    end
end
A

B = fill(0, (m, n))
for i in 1:m, j in 1:n
    B[i, j] = i + j
end
B
@assert A == B

#Exercises
for i=1:100
    println(i^2)
end

squares = Dict(1 => 1)
for i=1:100
    squares[i] = i^2;
end
println(squares) #You have to ensure conformity in the vartype of the parent dict declaration
println(sort(squares))

@assert squares[10] == 100
@assert squares[11] == 121

squares_arr = [i^2 for i=1:100]
@assert length(squares_arr) == 100
@assert sum(squares_arr) == 338350


#Conditionals
N = 10
if (N % 3 == 0) && (N % 5 == 0) # `&&` means "AND"; % computes the remainder after division
    println("FizzBuzz")
elseif N % 3 == 0
    println("Fizz")
elseif N % 5 == 0
    println("Buzz")
else
    println(N)
end

#ternary operator and short-circuit evaluation
x = 10; y = 1;
(x > y) ? x : y
(x > y) ? print("Yep!") : print("Na!")
(x > y) ? true : false

false && (println("hi"); true)
true && (println("hi"); true)

(x > 0) && error("x cannot be greater than 0")
true || println("hi")
false || println("hi")


#Exercises
numbers = [i^2 for i=1:10]

for num in numbers
    (num % 2 == 0) ? println(num, " is Even") : println(num, " is Odd")
end


















