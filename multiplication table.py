����� ����� ������ � �����, �� ��������� ������� ��������� �������������� �������. ��� ���������� ��� �� ����� ����������� ���������, ������� ���������� �� ���� ������� ���������.�������� ���������, �� ���� ������� ������ ������ ����� aa, bb, cc � dd, ������ � ����� ������. ��������� ������ ������� �������� ������� ��������� ��� ���� ����� ������� [a;b]ab �� ��� ����� ������� [c;d]cd.����� aa, bb, cc � dd �������� ������������ � �� ����������� 10, a?bab, c?dcd.�������� ������� ������ �� �������, ��� ���������� ��������� ������ ������ ����������� '\t' � ������ ���������. ��������, ��� ����� �������� � ������� ������� ��������� ���� ����� �� �������� �������� � ������������ ������� � ������ �������.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a and b and c and d <= 10:
    for i in range(c,d+1):
        print( "\t"+ str(i), end='')
    print(end="\n")
    for i in range (a,b+1):
            print(str(i)+"\t", end='')
            for j in range (c,d+1):
                print(str(i*j), end="\t")
            print("\n", end="")