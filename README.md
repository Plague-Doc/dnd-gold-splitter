# DnD Gold Splitter
This is a Discord bot made to specifically split found coins equally between any number of players in a DnD game.
After being added to a server, it takes in text from any channel specifically starting with the `!split` command, then followed by parameters split with a space.

## Available commands
* `!split ping` - Returns "Pong!" as a simple latency test.<br/>
* `!split help` - Returns a quick summary on formatting of commands and accepted coin types.<br/>
* `!split [number of people] [coin amount][coin type] ...` - The main command used to split coins.<br/>


## Examples
* `!split 4 25gp 96sp 21cp` - Splits 25 gold, 96 silver and 21 copper between 4 people.<br/>
* `!split 5 2gp 3cp` - There doesn't need to be all 3 types present at once for it to work.<br/>
* `!split 2 8sp 16sp` - You can even have the same type multiple times!

## Extra Info
* Accepted coin types are: `gp (Gold Points)` `sp (Silver Points)` `cp (Copper Points)`.
* The conversion rate between coin types is 100, as in `100 Copper = 1 Silver`, and `100 Silver = 1 Gold`.
* The bot automatically converts them before giving the total per person.
