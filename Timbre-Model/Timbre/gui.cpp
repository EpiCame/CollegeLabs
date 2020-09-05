#include "gui.h"


void gui::init_gui() {

	main_ly = new QVBoxLayout;
	this->setLayout(main_ly);
	model = new list_model(this->srv.get_all());
	lst = new QListView;
	lst->setModel(model);
	if(this->srv.get_all().empty())
			lst->setStyleSheet("background - color: grey; ");
	form = new QFormLayout;
	id_box = new QLineEdit;
	nume_box = new QLineEdit;
	an_box = new QLineEdit;
	tara_box = new QLineEdit;
	pret_box = new QLineEdit;
	form->addRow(new QLabel("Id: "), id_box);
	form->addRow(new QLabel("Nume: "), nume_box);
	form->addRow(new QLabel("An: "), an_box);
	form->addRow(new QLabel("Tara: "), tara_box);
	form->addRow(new QLabel("Pret: "), pret_box);
	lst_ly = new QHBoxLayout;
	lst_ly->addWidget(lst);
	lst_ly->addLayout(form);
	main_ly->addLayout(lst_ly);
	btns_ly = new QHBoxLayout;
	add_btn = new QPushButton("Adauga");
	spin = new QSpinBox;
	gen_btn = new QPushButton("Genereaza");
	exp_btn = new QPushButton("Exporta");
	exp_file = new QLineEdit;


	btns_ly->addWidget(add_btn);
	btns_ly->addWidget(gen_btn);
	btns_ly->addWidget(spin);
	btns_ly->addWidget(exp_btn);
	btns_ly->addWidget(exp_file);
	main_ly->addLayout(btns_ly);


}

void gui::connect_model() {

	QObject::connect(lst->selectionModel(), &QItemSelectionModel::selectionChanged, [&]() {
		if (lst->selectionModel()->selectedIndexes().empty()) {
			id_box->setText("");
			nume_box->setText("");
			an_box->setText("");
			tara_box->setText("");
			pret_box->setText("");
			return;
		}
		auto ind = lst->selectionModel()->selectedIndexes().at(0);
		QString str = ind.data(Qt::DisplayRole).toString();
		string line = str.toStdString();
		string elems[4];
		int i = 0;
		string aux;
		while (!line.empty()) {
			if (line.front() == ',') {
				line.erase(line.begin());
				elems[i++] = aux;
				aux.clear();
			}
			aux.push_back(line.front());
			line.erase(line.begin());
		}
		id_box->setText(QString::fromStdString(elems[0]));
		nume_box->setText(QString::fromStdString(elems[1]));
		an_box->setText(QString::fromStdString(elems[2]));
		tara_box->setText(QString::fromStdString(elems[3]));
		pret_box->setText(QString::fromStdString(aux));
		return;
		
		});

};

void gui::connect_sign_slot() {
	connect_model();

	QObject::connect(add_btn, &QPushButton::clicked, [&]() {
		int id = atoi(id_box->text().toStdString().c_str());
		string nume = nume_box->text().toStdString();
		int an = atoi(an_box->text().toStdString().c_str());
		int pret = atoi(pret_box->text().toStdString().c_str());
		string tara = tara_box->text().toStdString();
		id_box->setText("");
		nume_box->setText("");
		an_box->setText("");
		tara_box->setText("");
		pret_box->setText("");
		try {
			srv.add(id, nume, an, tara, pret);
			reload_list(srv.get_all());

		}
		catch (repo_exception& e) {
			QMessageBox::warning(this, "Warning", QString::fromStdString(e.get_msg()));
		}
		catch (valid_exception& e) {
			QMessageBox::warning(this, "Warning", QString::fromStdString(e.get_msg()));
		}
		});

	QObject::connect(gen_btn, &QPushButton::clicked, [&]() {
		string alpha{ "abcdefghijklmnoprstuivxzwy" };
		int nr = spin->value();
		this->srv.clear_timbre();
		srand(time(NULL));
		while (nr) {
			int lg_nume = rand() % 10 + 3;
			int lg_tara = rand() % 10 + 3;
			int id = rand() % 100;
			int an = rand() % 100 + 1000;
			int pret = rand() % 200;
			string nume(lg_nume, ' ');
			string tara(lg_tara, ' ');
			for (int i = 0; i < lg_nume; i++) {
				int ind = rand() % alpha.size();
				nume[i] = alpha[ind];
			}
			for (int i = 0; i < lg_tara; i++) {
				int ind = rand() % alpha.size();
				tara[i] = alpha[ind];
			}
			try {
				srv.add(id, nume, an, tara, pret);
				nr--;
			}
			catch (repo_exception&){}
			catch(valid_exception&){}
			reload_list(srv.get_all());
		}
		
		});

	QObject::connect(exp_btn, &QPushButton::clicked, [&]() {
		string file = exp_file->text().toStdString();
		ofstream g(file);
		if (!g.is_open())
			throw repo_exception("Cant open the file!\n");
		for (const auto& tb : srv.get_all())
			g << tb.to_str() << '\n';
		srv.clear_timbre();
		reload_list(srv.get_all());
		});
};

void gui::reload_list(vector<timbru>& timbs) {
	delete model;
	model = new list_model{ timbs };
	lst->setModel(model);
	connect_model();
};

