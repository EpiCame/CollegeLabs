#pragma once
#include <qwidget.h>
#include <qlistview.h>
#include <qlineedit.h>
#include <qmessagebox.h>
#include <qpushbutton.h>
#include <qlayout.h>
#include <qformlayout.h>
#include <qspinbox.h>
#include "service.h"
#include "list_model.h"
#include <qcolor.h>
#include <qpalette.h>
#include <qspinbox.h>
#include <qlabel.h>

class gui : public QWidget {

private:
	service& srv;


	void reload_list( vector<timbru>& timbs);

	//main layout 
	QVBoxLayout* main_ly;

	QFormLayout* form;
	QLineEdit* id_box;
	QLineEdit* nume_box;
	QLineEdit* an_box;
	QLineEdit* tara_box;
	QLineEdit* pret_box;

	QListView* lst;
	QPushButton* add_btn;
	QHBoxLayout* btns_ly;
	QHBoxLayout* lst_ly;
	QSpinBox* spin;
	QPushButton* gen_btn;

	QLineEdit* exp_file;
	QPushButton* exp_btn;

	list_model* model;

	void connect_model();

	void connect_sign_slot();

	void init_gui();
public:

	gui(service& srv) : srv{ srv } {
		init_gui();
		lst->setUniformItemSizes(true);
		connect_sign_slot();
	};



};


