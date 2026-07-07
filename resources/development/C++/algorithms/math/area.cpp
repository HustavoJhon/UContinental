/**
 * @details The area of a shape is the amount of 2D space it takes up.
 * All shape have a formula to get the area of any given shape.
 * These implementations support multiple return types.
 */ 

#define _USE_MATH_DEFINES
#include <cassert> /// for assert 
#include <cmath>    /// for M_PI definition and pow() 
#include <cstdint>  /// for uint16_t datatype
#include <iostream> /// for IO operations 

namespace math {

template <typename T> // Square (l * l)
T square_area(T length) {
  return length * length;
}

template <typename T> // Rectangle (l * w)
T rect_area(T length, T width) {
  return length * width;
}

template <typename T> // Triangle (b * h)
T triangle_area(T base, T height) {
  return base * height / 2;
}

template <typename T> // Circle (pi * r^2)
T circle_area(T redius) {
  return M_PI * pow(redius, 2);
}

template <typename T> // Parallelogram (b * h)
T parallelogram_area(T base, T height){
  return base * height;
}

template <typename T> // Cube (6 * (l * l))
T cube_surface_area(T length) {
  return 6 * length * length;
}

template <typename T> // Sphere (4 * pi * r^2)
T sphere_surface_area(T radius) {
  return 4 * M_PI * pow(radius, 2);
}

template <typename T> // Cylinder (2 * pi * r * h + 2 * pi * r^2)
T cylinder_surface_area(T radius, T height) {
  return 2 * M_PI * radius * height + 2 * M_PI * pow(radius, 2);
}

template <typename T> // Surface (3 * pi * r^2)
T hemi_sphere_surface_area(T radius) {
  return 3 * M_PI * pow(radius, 2);
}
} // namespace math


static void test() {
  // I/O variables for testing
  uint16_t int_length = 0;    // 16 bit integer length input
  uint16_t int_width = 0;     // 16 bit integer width input
  uint16_t int_base = 0;      // 16 bit integer base input
  uint16_t int_height = 0;    // 16 bit integer height input
  uint16_t int_expected = 0;  // 16 bit integer expected output
  uint16_t int_area = 0;      // 16 bit integer output

  float float_length = NAN;    // float length input
  float float_expected = NAN;  // float expected output
  float float_area = NAN;      // float output

  double double_length = NAN;    // double length input
  double double_width = NAN;     // double width input
  double double_radius = NAN;    // double radius input
  double double_height = NAN;    // double height input
  double double_expected = NAN;  // double expected output
  double double_area = NAN;      // double output

  // 1st test
  int_length = 5;
  int_expected = 25;
  int_area = math::square_area(int_length);

  std::cout << "AREA OF A SQUARE (int)" << std::endl;
  std::cout << "Input Length: " << int_length << std::endl;
  std::cout << "Expected Output: " << int_expected << std::endl;
  std::cout << "Output: " << int_area << std::endl;
  assert(int_area == int_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 2nd test
  float_length = 2.5;
  float_expected = 6.25;
  float_area = math::square_area(float_length);

  std::cout << "AREA OF A SQUARE (float)" << std::endl;
  std::cout << "Input Length: " << float_length << std::endl;
  std::cout << "Expected Output: " << float_expected << std::endl;
  std::cout << "Output: " << float_area << std::endl;
  assert(float_area == float_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 3rd test
  int_length = 4;
  int_width = 7;
  int_expected = 28;
  int_area = math::rect_area(int_length, int_width);

  std::cout << "AREA OF A RECTANGLE (int)" << std::endl;
  std::cout << "Input Length: " << int_length << std::endl;
  std::cout << "Input Width: " << int_width << std::endl;
  std::cout << "Expected Output: " << int_expected << std::endl;
  std::cout << "Output: " << int_area << std::endl;
  assert(int_area == int_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 4th test
  double_length = 2.5;
  double_width = 5.7;
  double_expected = 14.25;
  double_area = math::rect_area(double_length, double_width);

  std::cout << "AREA OF A RECTANGLE (double)" << std::endl;
  std::cout << "Input Length: " << double_length << std::endl;
  std::cout << "Input Width: " << double_width << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 5th test
  int_base = 10;
  int_height = 3;
  int_expected = 15;
  int_area = math::triangle_area(int_base, int_height);

  std::cout << "AREA OF A TRIANGLE" << std::endl;
  std::cout << "Input Base: " << int_base << std::endl;
  std::cout << "Input Height: " << int_height << std::endl;
  std::cout << "Expected Output: " << int_expected << std::endl;
  std::cout << "Output: " << int_area << std::endl;
  assert(int_area == int_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 6th test
  double_radius = 6;
  double_expected = 113.09733552923255;  // rounded down because the double datatype
              // truncates after 14 decimal places
  double_area = math::circle_area(double_radius);

  std::cout << "AREA OF A CIRCLE" << std::endl;
  std::cout << "Input Radius: " << double_radius << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 7th test
  int_base = 6;
  int_height = 7;
  int_expected = 42;
  int_area = math::parallelogram_area(int_base, int_height);

  std::cout << "AREA OF A PARALLELOGRAM" << std::endl;
  std::cout << "Input Base: " << int_base << std::endl;
  std::cout << "Input Height: " << int_height << std::endl;
  std::cout << "Expected Output: " << int_expected << std::endl;
  std::cout << "Output: " << int_area << std::endl;
  assert(int_area == int_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 8th test
  double_length = 5.5;
  double_expected = 181.5;
  double_area = math::cube_surface_area(double_length);

  std::cout << "SURFACE AREA OF A CUBE" << std::endl;
  std::cout << "Input Length: " << double_length << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 9th test
  double_radius = 10.0;
  double_expected = 1256.6370614359172;  // rounded down because the whole
                                           // value gets truncated
  double_area = math::sphere_surface_area(double_radius);

  std::cout << "SURFACE AREA OF A SPHERE" << std::endl;
  std::cout << "Input Radius: " << double_radius << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 10th test
  double_radius = 4.0;
  double_height = 7.0;
  double_expected = 276.46015351590177;
  double_area = math::cylinder_surface_area(double_radius, double_height);

  std::cout << "SURFACE AREA OF A CYLINDER" << std::endl;
  std::cout << "Input Radius: " << double_radius << std::endl;
  std::cout << "Input Height: " << double_height << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;

  // 11th test
  double_radius = 10.0;
  double_expected = 942.4777960769379;
  double_area = math::hemi_sphere_surface_area(double_radius);

  std::cout << "SURFACE AREA OF A HEMI-SPHERE" << std::endl;
  std::cout << "Input Radius: " << double_radius << std::endl;
  std::cout << "Expected Output: " << double_expected << std::endl;
  std::cout << "Output: " << double_area << std::endl;
  assert(double_area == double_expected);
  std::cout << "TEST PASSED" << std::endl << std::endl;
}

int main() {
  test();
  return 0;
}
