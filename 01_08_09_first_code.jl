# writing function for the Babylonian
function Babylonian(x; N = 10)
    t = (1+x)/2
    for i = 2: N; t = (t+x/t)/2 end
    t
end

# variable declaration and function call
α = π; Babylonian(α), sqrt(α)
x = 2; Babylonian(x), sqrt(x)

#sum and quotient derivatives function
struct D <: Number
    f::Tuple{Float64, Float64}
end

import Base:+, /, convert, promote_rule
+(x::D, y::D) = D(x.f .+ y.f)
/(x::D, y::D) = D((x.f[1]/y.f[1], (y.f[1]*x.f[2] - x.f[1]*y.[2])/y.f[1]^2))
convert(::Type{D}, x::Real) = D((x, zero(x)))
promote_rule(::Type{D}, ::Type{<:Number}) = D

#variable and function test
x = 49; Babylonian(D((x,1))), (sqrt(x), .5/sqrt(x))
x = π; Babylonian(D((x,1))), (sqrt(x), .5/sqrt(x))


#derivative Babylonian
function dBabylonia(x; N = 10)
    t = (1+x)/2
    m = 1/2
    for i = 1:N;
        t = (t + x/t)/2;
        m = (m+(t-x*m)/t^2)/2;
    end
    m
end

#variable testing
x = π; dBabylonia(x), .5/sqrt(x)

#istanbul_sin
function istanbul_sin(x)
    t = 0
    for i=1:10
        t -= (-1.0)^i*(x)^(2*i-1)/prod(1:(2*i-1))
    end
    t
end

istanbul_sin(D((1.0, 1.0)))


A = randn(3,3)
x = randn(3)





















