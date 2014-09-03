flag = True;
num = 50;
high = 100;
low = 0;
while(flag):
    print("Is your secret number "+ str(num) + "?")
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == h:
        high = num
        num = (high + low)/2
    elif ans == l:
        low = num
        num = (high + low)/2
    elif ans == c:
        print("Game over. Your secret number was: "+ str(num))
        flag = Flase
    else:
        print("Sorry, I did not understand your input.");
