class Arithmetic
{
    constructor(A,B)
    {
        this.No1 = A;
        this.No2 = B;
    }

    Addition()
    {
        return this.No1 + this.No2
    }

    Substraction()
    {
        return this.No1 - this.No2
    }
}

function main()
{
    let aobj = new Arithmetic(11,10)

    console.log(aobj.Addition())
    console.log(aobj.Substraction())
}

main()
