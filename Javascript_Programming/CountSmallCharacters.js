let iCount = 0

function CountSmall(str)
{
    for(let i = 0; i < str.length; i++)
    {
        if(str[i] >= 'a' && str[i] <= 'z')
        {
            iCount++
        }
    }

    return iCount
}

function main()
{
    let name = "Marvellous"

    let iRet = 0

    iRet = CountSmall(name)

    console.log("Small Characters are : ",iRet)
}

main()
