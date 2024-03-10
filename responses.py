import math

def get_response(user_input: str) -> str:
    input: list[str] = user_input.lower().split()

    if len(input) == 2 and input[1] == "ping":
        return "Pong!"
    
    elif len(input) == 2 and input[1] == "help":
        return """Command template:
`!split [number of people] [coin amount][coin type] ...`

Accepted coin types: gp, sp, cp (gold, silver, copper)

Example inputs:
`!split 4 25gp 96sp 21cp`  `!split 5 2gp 3cp`  `!split 2 8sp 16sp`"""
    
    elif int(input[1]) == 0:
        return "Cannot devide by 0."

    else:
        try:
            total_copper: int = 0
            total_silver: int = 0
            total_gold: int = 0
            leftover_copper: int = 0
            error_thrown: bool = False

            for x in range(2, len(input)):
                if input[x][len(input[x]) - 2:] == "gp":
                    total_copper += int(input[x][:len(input[x]) - 2]) * 100
                elif input[x][len(input[x]) - 2:] == "sp":
                    total_copper += int(input[x][:len(input[x]) - 2]) * 10
                elif input[x][len(input[x]) - 2:] == "cp":
                    total_copper += int(input[x][:len(input[x]) - 2])

            leftover_copper = total_copper % int(input[1])
            total_copper -= leftover_copper
            total_copper = int(float(total_copper) / int(input[1]))

            if total_copper / 100 >= 1:
                total_gold = math.floor(total_copper / 100)
                total_copper -= total_gold * 100

            if total_copper / 10 >= 1:
                total_silver = math.floor(total_copper / 10)
                total_copper -= total_silver * 10

            total_copper = int(total_copper)

        except Exception as e:
            error_thrown = True
            print(f"[DEBUG] {e}")

        if error_thrown == False:
            output_string: str = f"Per person:"

            if total_gold >= 1:
                output_string += f" `{total_gold}gp`"

            if total_silver >= 1:
                output_string += f" `{total_silver}sp`"

            if total_copper >= 1:
                output_string += f" `{total_copper}cp`"

            if total_gold < 1 and total_silver < 1 and total_copper < 1:
                output_string = "Indivisible equally :("
            elif leftover_copper >= 1:
                output_string += f"\nCopper left behind: `{leftover_copper}`"

            return output_string

    return "Invalid input, try `!split help`"
 
# FOR TESTING
if __name__ == '__main__':
    terminal_input: str = input()
    terminal_output: str = get_response(terminal_input)
    print(terminal_output)