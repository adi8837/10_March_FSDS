def door_mat_dim(N):
  if N % 2 == 0:
    return "N must be an odd number."
  M = 3 * N
  pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
  welcome_line = 'WELCOME'.center(M, '-')
  pattern.append(welcome_line)  

  # Create the mirrored pattern without the welcome message
  mirrored_pattern = pattern[::-1][1:]  # Excluding the first element (welcome line)

  pattern += mirrored_pattern
  return '\n'.join(pattern)

def main():
  N = int(input("Enter the number of rows (must be odd): "))
  print(door_mat_dim(N))

if __name__ == "__main__":

  main()