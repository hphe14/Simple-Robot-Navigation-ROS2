#include <vector>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/float32_multi_array.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <string>

using std::placeholders::_1;
using namespace std::chrono_literals;

class ControllerInputSub : public rclcpp::Node
{
  public:
    ControllerInputSub()
    : Node("input_sub")
    {
      subscription_ = this->create_subscription<std_msgs::msg::Float32MultiArray>(
      "input_topic", 10, std::bind(&ControllerInputSub::topic_callback, this, _1));

      publisher_ = this->create_publisher<geometry_msgs::msg::Twist>(
      "/cmd_vel", 10);
    }
    
  private:
    void topic_callback(const std_msgs::msg::Float32MultiArray & msg) const
    {
      float steer = (msg.data[0]) *-1;
      float backwards = (msg.data[1] + 1)* -1 ;
      float forwards = msg.data[2] + 1;
      //float constspeed_B = msg.data[3];
      //float constspeed_A = msg.data[4];

      //std::cout << steer << std::endl;
      auto message = geometry_msgs::msg::Twist();
      message.linear.x = forwards + backwards;

      //message.angular.z = steer ;
      if (backwards < 0){
        message.angular.z = steer*-1;
      }
      else{
        message.angular.z = steer;
      }
      publisher_->publish(message);
    }
    rclcpp::Subscription<std_msgs::msg::Float32MultiArray>::SharedPtr subscription_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
   
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ControllerInputSub>());
  rclcpp::shutdown();
  return 0;
}