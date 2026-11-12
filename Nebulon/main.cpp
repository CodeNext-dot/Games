#include <SFML/Graphics.hpp>
using namespace std;
using namespace sf;

void acoes_personagem(RenderWindow& window, RectangleShape& person) {
    if (Keyboard::isKeyPressed(Keyboard::Key::D)) {
        person.move({ 10.f, 0.f });
    }
    if (Keyboard::isKeyPressed(Keyboard::Key::A)) {
        person.move({ -10.f, 0.f });
    }
}

void atirar(RectangleShape& person, CircleShape& tiro) {
    Clock clock;
    tiro.setPosition({person.getPosition().x + ((person.getSize().x / 2) - tiro.getRadius()), person.getPosition().y});
    tiro.move({0.f, -1.f * clock.restart().asSeconds() });
}

int main()
{
    unsigned int posX = 800, posY = 600;
    float posXf = static_cast<float>(posX), posYf = static_cast<float>(posY);

    RenderWindow window{
        VideoMode({posX, posY}),
        "Minha Hello world"
    };

    RectangleShape homem({50, 50}); homem.setFillColor(Color::White); homem.setPosition({(posXf / 2) - 25.f, posYf - 55.f});
    CircleShape tiro(5.f); tiro.setFillColor(Color::Yellow); tiro.setPosition({posXf, 0.f});


    while (window.isOpen())
    {
        while (const optional event = window.pollEvent())
        {
            if (event->is<Event::Closed>()) {
                window.close();
            }
            if (event->is<Event::KeyPressed>()) {
                acoes_personagem(window, homem);
                if (Keyboard::isKeyPressed(Keyboard::Key::E)) {
                    
                }
            }
                
        }


        window.clear();
        window.draw(homem);
        window.draw(tiro);
        window.display();
    }
}