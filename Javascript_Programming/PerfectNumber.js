
function CheckPerfect(No)
{
     let i = 0
     let sum = 0

     for(i = 1; i <= No/2; i++)
     {
          if(No % i == 0)
          {
               sum = sum + i
          }
     }

     return (No == sum)
}

function main()
{
     let bRet = false

     bRet = CheckPerfect(28)

     if(bRet == true)
     {
          console.log("It is Perfect number")
     }
     else
     {
          console.log("It is not Perfect number")
     }
}

main()
