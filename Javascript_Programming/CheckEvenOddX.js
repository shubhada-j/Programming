function CheckEven(No)
{
    if (No % 2 == 0)
    {
        return true
    }
    else
    {
        return false
    }
}

function main()
{
   let value = 11

   let bRet = false

   bRet = CheckEven(value)

   if(bRet == true)
   {
        console.log(`${value} is even number`)
   }
   else
   {
        console.log(`${value} is odd number`)
   }

}

main()
