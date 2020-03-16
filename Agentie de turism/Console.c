#include "Console.h" 
#include <stdio.h>
#include <string.h>
/*
Adauga o oferta citita de la tastatura in agency
*/
void adauga_oferta(Agency* agency) {
	printf("Type:");
	char type[15];
	scanf_s("%s", type, sizeof(type));
	printf("Destination: ");
	char destination[50];
	scanf_s("%s", destination, sizeof(destination));
	printf("Date:\nDay:");
	Date d;
	scanf_s("%d", &d.dd);
	printf("Month: ");
	scanf_s("%d", &(d.mm));
	printf("Year: ");
	scanf_s("%d", &(d.yy));
	printf("Price: ");
	float price;
	scanf_s("%f", &price);
	int add_code = add_ofert(agency, type, destination, d, price);
	switch (add_code)
	{
	case 0:
		printf("Added!\n");
		break;
	case 1:
		printf("Invalid type!\n");
		break;
	case 2:
		printf("Invalid date!\n");
		break;
	case 3:
		printf("Invalid destination!\n");
		break; 
	case 4:
		printf("Invalid price!\n");
		break; 
	default:
		break;
	}
}

/*
Sterge o oferta din agentie
*/
void sterge_oferta(Agency* agency) {
	printf("Position of offert: ");
	int poz;
	scanf_s("%d", &poz);
	int delete_code = delete_ofert(agency, poz);
	switch (delete_code) {
	case 0:
		printf("Deleted!\n");
		break;
	case 1:
		printf("Invalid position!\n");
		break;
	default:
		break;
	}
}


/*
Modifica oferta din agency cu una citita de la tastatura
*/
void modifica_oferta(Agency* agency) {
	printf("Position of offert: ");
	int poz;
	scanf_s("%d", &poz);
	printf("Type:");
	char type[15];
	scanf_s("%s", type, sizeof(type));
	printf("Destination: ");
	char destination[50];
	scanf_s("%s", destination, sizeof(destination));
	printf("Date:\nDay:");
	Date d;
	scanf_s("%d", &d.dd);
	printf("Month: ");
	scanf_s("%d", &(d.mm));
	printf("Year: ");
	scanf_s("%d", &(d.yy));
	printf("Price: ");
	float price;
	scanf_s("%f", &price);
	int modify_code = modify_ofert(agency, poz, type, destination, d, price);
	switch (modify_code)
	{
	case 0:
		printf("Modified!\n");
		break;
	case 1:
		printf("Invalid type!\n");
		break;
	case 2:
		printf("Invalid date!\n");
		break;
	case 3:
		printf("Invalid destination!\n");
		break;
	case 4:
		printf("Invalid price!\n");
		break;
	case 5:
		printf("Invalid position!\n");
		break;
	default:
		break;
	}
}	
/*
ordoneaza ofertele dupa pret, destinatie
*/
void ordoneaza_oferte(Agency* agency) {
	List ordered = order_oferts(agency);
	TElem o;
	int i;
	for (i = 0; i < size(&ordered); i++)
	{
		o = get(&ordered, i);
		printf("%s, %s, %d-%d-%d, %f\n", get_type(&o), get_destination(&o), get_date(&o).dd, get_date(&o).mm, get_date(&o).yy, get_price(&o));
	}
	destroy(&ordered);
}

/*
Permite citirea unui tip si afisarea ofertelor cu acel tip
*/
void filtreaza_oferte(Agency* agency) {
	char type[15];
	printf("Type: ");
	scanf_s("%s", type, sizeof(type));
	//validate type 
	if (strcmp(type, "munte") != 0 &&
		strcmp(type, "mare") != 0 &&
		strcmp(type, "city break") != 0)
		printf("Invalid type!\n");
	List filtered = filter_oferts(agency, type);
	if (size(&filtered) == 0)
		printf("There are no offerts with that type!\n");
	else
	{
		TElem o;
		int i;
		for (i = 0; i < size(&filtered); i++)
		{
			o = get(&filtered, i);
			printf("%s, %s, %d-%d-%d, %f\n", get_type(&o), get_destination(&o), get_date(&o).dd, get_date(&o).mm, get_date(&o).yy, get_price(&o));
		}
	}
	destroy(&filtered);
}

/*
Tipareste ofertele dintr o agentie
*/
void tipareste_oferte(Agency* agency) {
	List oferte = get_all(agency);
	TElem o;
	int i = 0;
	for (i = 0; i < size(&oferte); i++)
	{
		o = get(&oferte, i);
		printf("%d: %s, %s, %d-%d-%d, %f\n", i, get_type(&o), get_destination(&o), get_date(&o).dd, get_date(&o).mm, get_date(&o).yy, get_price(&o));
	}
	destroy(&oferte);
}


void run(){
	Agency agency = create_agency();
	int ruleaza = 1;
	while (ruleaza) {
		printf("1 Add offert\n2 Modify offert\n3 Delete offert\n4 Order by price, destination\n5 Filter by type\n6 Print all offerts\n0 Exit\nCommand:");
		int cmd = 0;
		scanf_s("%d", &cmd);
		switch (cmd) {
		case 0:
			ruleaza = 0;
			break;
		case 1:
			adauga_oferta(&agency);
			break;
		case 2:
			modifica_oferta(&agency);
			break;
		case 3:
			sterge_oferta(&agency);
			break;
		case 4:
			ordoneaza_oferte(&agency);
			break;
		case 5:
			filtreaza_oferte(&agency);
			break;
		case 6:
			tipareste_oferte(&agency);
			break;
		default:
			printf("Comanda invalida!\n");
		}
	}
	destroy_agency(&agency);
}


