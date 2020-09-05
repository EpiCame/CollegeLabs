#pragma once
#include <qabstractlistmodel>
#include "model.h"
#include <vector>
#include <qstring.h>

class list_model : public QAbstractListModel {

private:
	vector<timbru>& timbs;

public:
	list_model(vector<timbru>& timbs) :timbs{ timbs } {
	
	};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override {
		return timbs.size();
	};

	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
		if (role == Qt::DisplayRole) {
			return QString::fromStdString(timbs[index.row()].to_str());
		}
		return QVariant{};
	};

	void set_timbre(const vector<timbru>& timb) {
		this->timbs = timb;
		auto tl = createIndex(0, 0);
		auto br = createIndex(timb.size(), 0);
		emit dataChanged(tl, br);

	}
};
