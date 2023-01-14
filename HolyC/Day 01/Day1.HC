Cd("C://Home/AoC/Day1/");

U8 *WordParse(U8 *str) {
	while ('\n'!=*str) str++;
	return str;
}

I64 N = 1000; // stupid table number because i don't want to calculate length

I64 table[N];

U0 dump() {
	I64 i;
	for (i=0; i<N; i++){
		"%7d", table[i];
	}
}

U0 tableBuild() {
	I64 size;
	I64 x;
	U8 *file = FileRead("adventofcodeelves.TXT", &size);$IV,0$
	U8 *str = file;
	U8 *endPointer;
	I64 i = 0;
	while (size > 1) {
		//"%s\n", str;
		//"%d\n", size;
		I64 n = endPointer -str;
		//"%d\n", n;
		endPointer = WordParse(str);
		x = Str2I64(str, 10, &endPointer); 
		//"%d\n", x;
		table[i] += x;
	
		str = endPointer;
		if ('\n' == *(str+1)) {
			i++;
		}
		size -= endPointer-str+1;
	}
	Free(file);
	//dump;	
}

U0 ArraySort() {
	I64 i;
	for (i=0; i<N; i++) {
		I64 j;
		for (j = i+1; j<N; j++) {
			if (table[i] < table[j]) {
				I64 temp = table[i];
				table[i] = table[j];
				table[j] = temp;
			}
		}
	}
}


MemSet(table, 0, sizeof(I64)*N);

tableBuild;
ArraySort;

"\n Part 1: %5d \n Part 2 %6d \n", table[0], table[0]+table[1]+table[2];

