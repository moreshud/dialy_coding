versioninfo()

using Plots
pyplot()
plot(rand(4,4))

#data types
my_string1 = " Hello"
my_string2 = "World!"
join([my_string1, my_string2], " ")
replace(my_string1, "H" => "h")
strip(my_string1)


A = []; A = Int64[];
a = zeros(5)
a = [1;2;3]; a = [1,2,3]
a = [[1, 2, 3] [4,  5, 6]]
a = [1 4; 2 5; 3 6]
a = [[1,2,3],[4,5,6]]


a = 1,2,3 #(1,2,3)
v = [a...] 
w = [i[1] for i in a]
x = collect(a)

mydict = Dict('a'=>1, 'b'=>2, 'c'=>3)
for (k,v) in mydict
    println("$k is $v")
 end

a = Set([1,2,2,3,4]) 
b = Set([5,2,2,3,6])
union(a, b)
intersect(a,b)
setdiff(a,b)


#control flow
for i=1:2,j=2:4
    println(i*j)
end

a = [i for i in [1,2,3]]
x + 2y for x in [10,20,30], y in [1,2,3]]

other similar comprehension support

#function
function f(x)
    x+2
end

f(2), f(.9), f(-1000.5)

values = [1,2,3]
function average(init, args...) #The parameter that uses the ellipsis must be the last one
  s = 0
  for arg in args 
    s += arg 
  end
  return init + s/length(args)
end
a = average(10,1,2,3)        # 12.0
a = average(10, values ...)  # 12.0

myfunction(a,b) = a*2,b+2
x,y = myfunction(1,2)


x -> x^2 + 2x - 1 #anonymous function
(x,y,z) -> x + y + z


#structure or class object
struct Person
  myname::String
  age::Int64
end

struct Shoes
   shoesType::String
   colour::String
end

struct Student
   s::Person
   school::String
   shoes::Shoes
end

function printMyActivity(self::Student)
   println("I study at $(self.school) school")
end

struct Employee
   s::Person
   monthlyIncomes::Float64
   company::String
   shoes::Shoes
end

function printMyActivity(self::Employee)
  println("I work at $(self.company) company")
end

gymShoes = Shoes("gym","white")
proShoes = Shoes("classical","brown")

Marc = Student(Person("Marc",15),"Divine School",gymShoes)
MrBrown = Employee(Person("Brown",45),1200.0,"ABC Corporation Inc.", proShoes)

printMyActivity(Marc)
printMyActivity(MrBrown)

#reference: https://syl1.gitbook.io/julia-language-a-concise-tutorial/language-core/input-output















