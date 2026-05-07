\ 🌍 地理空间数据区块链存证系统

\(Geospatial Data Blockchain Notarization System)\



!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

!\[Solidity](https://img.shields.io/badge/Solidity-%5E0.8.8-363636.svg)

!\[Python](https://img.shields.io/badge/Python-3.x-blue.svg)

!\[Network](https://img.shields.io/badge/Network-Sepolia-lightgrey.svg)



> 基于区块链技术的地理空间数据存证系统，利用以太坊 \\Sepolia 测试网\\实现文件哈希存证、时间戳记录和防篡改验证。



\---



\📖 一、项目背景



在地理信息系统（GIS）领域，数据来源的可信性和时效性至关重要。本项目通过智能合约将文件哈希（Hash）上传至以太坊 Sepolia 测试网，利用区块链\*\*去中心化\*\*和\*\*不可篡改\*\*的特性，为地理空间数据提供公开、透明、可验证的存在证明（Proof of Existence）。


🛠 二、技术栈

| 类别 | 技术方案 | 说明 |
| :--- | :--- | :--- |
| **智能合约** | Solidity `^0.8.8` | 核心存证逻辑实现 |
| **部署工具** | Remix IDE + MetaMask | 合约编译与发布部署 |
| **区块链网络** | Sepolia Testnet | 以太坊官方测试网 |
| **交互脚本** | Python 3 + Web3.py | 与链上合约进行数据交互 |
| **节点服务** | Infura | 提供 RPC 接口接入以太坊网络 |
| **版本控制** | Git + GitHub | 代码托管与版本管理 |



\⚙️ 三、环境配置



\ 1. 克隆仓库

将本项目克隆到本地机器并进入项目目录：

```bash

git clone https://github.com/zhanglinguo/geospatial-data-blockchain.git

cd geospatial-data-blockchain

```



\ 2. 安装依赖

确保本地已安装 Python 3 环境，然后安装 Web3.py 库：

```bash

pip install web3

```



\ 3. 配置敏感信息（⚠️ 重要）

在项目根目录创建 `config.py` 文件。该文件已被加入 `.gitignore`，\*\*请勿将其提交到公开仓库\*\*以免泄露私钥。



在 `config.py` 中填入以下内容：

```python

\ config.py



\ 你的 Infura RPC 节点地址

WEB3\_PROVIDER = "https://sepolia.infura.io/v3/你的Infura项目ID"



\ 智能合约地址

CONTRACT\_ADDRESS = "0x449CBAF621E7b28577530779395C182b1398D725"



\ 你的钱包私钥（⚠️ 注意：不要加 0x 前缀，且确保该测试钱包内有 Sepolia ETH 余额）

PRIVATE\_KEY = "你的钱包私钥"   

```

> \\💡 提示\\：如果你的钱包中没有 Sepolia 测试币 (Sepolia ETH)，请前往 \[Sepolia Faucet](https://sepoliafaucet.com/) 免费领取。



\ 🚀 四、运行测试



\ 1. 上传文件哈希（需消耗 Gas 费）

运行上传脚本，系统将计算目标数据文件的哈希值，并将其打包成交易发送到区块链上。

```bash

python upload\_hash.py

```

\\✅ 成功输出示例：\\

```text

文件哈希：04e97b50852bc83d355ba3a87d963a782714cf1b61783f94dc0054cb59b30

交易已发送，哈希：0x7a2f...

等待确认...

✅ 上链成功！区块高度：10773562

```



\ 2. 验证文件完整性（免费查询）

运行验证脚本，系统会重新计算本地文件的哈希，并去链上查询是否存在及对应的时间戳。

```bash

python verify\_hash.py

```

\\✅ 成功输出示例：\\

```text

✅ 文件哈希已在链上，未被篡改！

上链时间戳：1777736148 (2026-05-02 15:35:48)

```



\ 🛡️ 五、防篡改检测测试



为了验证区块链的防篡改特性，可以进行以下破坏性测试：



1\. 打开 `data/elevation\_sample.csv` 文件。

2\. 随意修改其中的\*\*任意一个数据或字符\*\*并保存。

3\. 再次运行验证脚本：

&#x20;  ```bash

&#x20;  python verify\_hash.py

&#x20;  ```

4\. \\❌ 预期输出：\\

&#x20;  ```text

&#x20;  ❌ 文件哈希未在链上，可能是新文件或已被篡改！

&#x20;  ```



\📜 六、核心合约说明



\- \\合约地址\\:\[`0x449CBAF621E7b28577530779395C182b1398D725`](https://sepolia.etherscan.io/address/0x449CBAF621E7b28577530779395C182b1398D725) (点击在 Sepolia Etherscan 上查看)



| 函数名 | 交互类型 | 说明 |

| :--- | :---: | :--- |

| `storeHash(string memory \_hash)` | 写（需 Gas） | 存储目标文件的哈希值及当前区块的时间戳 |

| `getTimestamp(string memory \_hash)` | 读（免费） | 根据哈希值查询其首次上链记录的时间 |

| `exists(string memory \_hash)` | 读（免费） | 检查某哈希值是否已经被安全记录在区块链上 |



\ 📂 七、项目结构



```text

geospatial-data-blockchain/

├── config.py               # ⚙️ 敏感配置（仅本地存在，不提交）

├── upload\_hash.py          # 📤 上传存证脚本

├── verify\_hash.py          # 🔍 验证比对脚本

├── .gitignore              # 🙈 Git 忽略规则

├── data/

│   └── elevation\_sample.csv   # 📊 待存证的地理空间数据样本

└── screenshots/            # 🖼️ 运行截图目录（可选）

```



\ 🗺️ 八、未来改进方向 (Roadmap)



\- \[ ] \*\*支持批量存证\*\*：优化脚本，支持一次性对整个文件夹内的多个数据文件进行哈希上链。

\- \[ ] \*\*可视化 Web 界面\*\*：开发基于 React + Web3.js / Ethers.js 的前端面板，降低使用门槛。

\-\[ ] \*\*IPFS 深度集成\*\*：不仅存证哈希，还将大体积的 GIS 原始文件存储至 IPFS 分布式网络。

\- \[ ] \*\*多链支持\*\*：将智能合约部署并兼容 Polygon、Arbitrum 等低 Gas 且高吞吐的二层（L2）网络。



\ 📄 九、许可证与联系方式



\- \*\*开源协议\*\*：本项目基于 \[MIT License](./LICENSE) 开源。

\- \*\*项目作者\*\*：\[zhanglinguo](https://github.com/zhanglinguo)

\- \*\*问题反馈\*\*：欢迎提交 \[Issues](https://github.com/zhanglinguo/geospatial-data-blockchain/issues) 或 Pull Requests 进行技术交流探讨！

