func checkLenEven(val int) bool{
    if val == 0{
        return false
    }
    count:=0
    for val!=0{
        val = val/10;
        count++
    }
    if count%2==0{
        return true
    }
    return false
}
func findNumbers(nums []int) int {
    sum:=0
    for _,value := range nums{
        if checkLenEven(value){
            sum++
        }
    }
    return sum
}