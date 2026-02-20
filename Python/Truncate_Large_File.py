input_file = '/Users/neevgrover/Documents/Lichess Stuff/July 2024 Lichess Games.pgn'
output_file = '/Users/neevgrover/Documents/Lichess Stuff/TruncatedJuly2024Games.pgn'
max_lines = 1000  # Adjust based on how much you want to keep
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for i, line in enumerate(infile):
        if i >= max_lines:
            break
        outfile.write(line)