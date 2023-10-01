def main():
  number_of_disc = 3
  from_peg = 1
  to_peg = 3
  temp_peg = 2
  move_disc(number_of_disc, from_peg, to_peg, temp_peg)

def move_disc(number_of_disc,from_peg, to_peg, temp_peg):
  if number_of_disc > 0:
    move_disc(number_of_disc - 1, from_peg, temp_peg, to_peg)
    print("Move a disc from peg", from_peg ,"to peg", to_peg)
    move_disc(number_of_disc - 1, temp_peg, to_peg, from_peg)

main()
