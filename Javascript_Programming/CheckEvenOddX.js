function CheckEven(No)
{
    return (No % 2 == 0)            
}

function main()
{
   let value = 12

   let bRet = false

   bRet = CheckEven(value)

   if(bRet)                         
   {
        console.log(`${value} is even number`)
   }
   else
   {
        console.log(`${value} is odd number`)
   }

}

main()

