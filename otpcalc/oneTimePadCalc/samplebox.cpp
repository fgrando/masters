#include "samplebox.h"
#include "ui_samplebox.h"

#include <QDebug>

sampleBox::sampleBox(QString encrypted, QWidget *parent) :
    QWidget(parent),
    ui(new Ui::sampleBox)
{
    ui->setupUi(this);
    ui->encrypted->setText(encrypted);
}

sampleBox::~sampleBox()
{
    delete ui;
}

bool sampleBox::validChar(int code)
{
    if (code < 0x20 || code > 0x7e)
        return false;
    return true;
}

void sampleBox::calculateXor(QString key)
{
    QString text = ui->encrypted->toPlainText();
    QString keyText = "";
    QString result = "";
    while(keyText.length() < text.length())
        keyText = keyText + key;

    for (int i = 0; i < text.length(); i++)
    {
        char a = text.at(i).toLatin1();
        char b = keyText.at(i).toLatin1();
        int xored = a ^ b;
        if (validChar((xored)))
            result = result + QString((char)xored);
        else
            result = result + "°";
    }
    ui->decrypted->clear();
    ui->decrypted->setText(result);
}

void sampleBox::selectChar(int charIdx)
{
    QString text, html;

    text = ui->encrypted->toPlainText();
    if (charIdx >= text.length())
    {
        ui->encrypted->clear();
        ui->encrypted->setPlainText(text);
        return;
    }

    if (text.at(charIdx) == '<')
        html = text;
    else
        html = highLight(text, charIdx);

    ui->encrypted->clear();
    if (html.length() > 0)
    {
        ui->encrypted->setHtml(html);
    }
    else
    {
        ui->encrypted->setPlainText(text);
    }
}

QString sampleBox::highLight(QString str, int idx)
{
    QString html = "";
    if (idx >= 0 && idx < str.length())
    {
        for (int i = 0; i < str.length(); i++)
        {
            if (validChar(str.at(i).toLatin1()))
            {
                if (i == idx)
                {
                    html = html +  "<font color=\"Red\">" + str.at(i) + "</font>";
                }
                else
                {
                    html = html + str.at(i);
                }
            }
            else
            {
                html = html +  "<font color=\"Yellow\">" + str.at(i) + "</font>";
            }
        }
    }
    qDebug()<<html;
    return html;
}
