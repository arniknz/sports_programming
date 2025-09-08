import sys


def main():
    n = []
    for _ in range(3):
        n.append(int(input()))
    print("YES" if sum(n) - max(n) > max(n) else "NO")

if __name__ == '__main__':
    main()
