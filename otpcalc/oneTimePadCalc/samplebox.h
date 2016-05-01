#ifndef SAMPLEBOX_H
#define SAMPLEBOX_H

#include <QWidget>

namespace Ui {
class sampleBox;
}

class sampleBox : public QWidget
{
    Q_OBJECT

public:
    explicit sampleBox(QString encrypted, QWidget *parent = 0);
    ~sampleBox();

    static QString highLight(QString str, int idx);
    static bool validChar(int code);

public slots:
    void calculateXor(QString key);
    void selectChar(int charIdx);

private:
    Ui::sampleBox *ui;
};

#endif // SAMPLEBOX_H
