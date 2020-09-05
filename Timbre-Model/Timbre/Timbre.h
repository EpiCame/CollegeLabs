#pragma once

#include <QtWidgets/QWidget>
#include "ui_Timbre.h"

class Timbre : public QWidget
{
    Q_OBJECT

public:
    Timbre(QWidget *parent = Q_NULLPTR);

private:
    Ui::TimbreClass ui;
};
