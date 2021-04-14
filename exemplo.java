long totalMilisegundos = System.currentTimeMillis() - 10800000;
		
		long totalsegundos = totalMilisegundos / 1000;
		long segundosAtual = totalsegundos % 60;
		
		long totalMinutos = totalsegundos / 60;
		long minutoAtual = totalMinutos % 60;
		
		long totalhora = totalMinutos / 60;
		
		long horaAtual = totalhora % 24;
		
		System.out.println(horaAtual + ":" + minutoAtual + ":" + segundosAtual);
		
		System.out.println("Total de Milisegundos des de 01-01-1970 : " + totalMilisegundos);

