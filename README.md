# sirireader
This is the workings of a standalone parser for Siri to use with the Shortcuts application

## Shortcuts Links and Usage

The shortcut currently works by using Siri to initiate the "Read me a story" shortcut which calls the "Read Loop" shortcut and reads the story.

The 'story' in this case is a prepared folder of text files that is iterated through by the shortcut. The only way to have this work is to store the folder (currently hardcoded to be hp5) in your iCloud shortcuts folder:

`iCloud/Shortcuts/read/hp5`

So this means *the method by which Siri can read you a story* is as follows:

1. Clone the repo to your desired location
2. Place the desired story in a text file in the /sirireader/input folder (currently hardcoded as hp5.txt)
3. Run the python3 script. This will put the parsed text files in the /sirireader/output folder
4. Move the output text files into the iCloud/Shortcuts/read/hp5 folder
5. Install the shortcuts linked above.
6. Add the "Read me a story" shortcut to Siri
7. With your phone unlocked, run the shortcut with siri by saying "Hey Siri, read me a story"
